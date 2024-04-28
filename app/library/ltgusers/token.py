from fastapi.responses import JSONResponse
from ..utilities.security import SecurityUtilities, credentails_exception
from sqlmodel import Session, SQLModel, select
from jose import JWTError, jwt
from passlib.context import CryptContext
import secrets
from datetime import datetime, timedelta, timezone
from models.usermodels import usermodels
from models.security.token import Token, TokenData, TokenTracker
from repositories.tokenrepo import TokenRepository
from repositories.usersrepo import UsersRepository
import os




class TokenHandler:
    SECRET_KEY: str = secrets.token_hex(32)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    TOKEN_REPOSITORY: TokenRepository = TokenRepository()
    USER_REPOSITORY: UsersRepository = UsersRepository()

    def __init__(self):
        meaning_of_life = os.environ.get('ltg_life_meaning')
        if meaning_of_life is not None:
            TokenHandler.SECRET_KEY = meaning_of_life
        else:
            os.environ['ltg_life_meaning'] = TokenHandler.SECRET_KEY
        
    
    async def decode(self, token: Token) -> usermodels.ltgUserBase:
        """
        Verifies and Decodes the given token and returns an instance of 
        ltgUserBase if validation is passed.

        Args:
            token (Token): The token to decode.

        Returns:
            usermodels.ltgUserBase: An instance of ltgUserBase representing the decoded token.

        Raises:
            credentails_exception: If the token is invalid, expired, or if the user is not found in the database.
        """
        # TODO: Logging, tray/catch, and error handling for all non credential exceptions
        # verify token
        if token is None or  token.access_token is None:
            raise credentails_exception # no token  
        token_from_db = TokenHandler.TOKEN_REPOSITORY.get(TokenTracker, token.access_token) # check if token is in DB
        if token_from_db is None:
            raise credentails_exception # token not found in DB 
        else: 
            if token_from_db.expire_time < int(datetime.now(timezone.utc).timestamp()):
                raise credentails_exception # token expired
        # Decode Token
        try:
            decoded_jwt = TokenData.model_construct(
                **jwt.decode(token.access_token, self.SECRET_KEY, algorithms=[self.ALGORITHM]))
        except JWTError:
            raise credentails_exception

        # build and return ltgUserBase instance
        user_from_db = TokenHandler.USER_REPOSITORY.get(usermodels.ltgUserBase, token_from_db.user_id)  
        if user_from_db is None:
            raise credentails_exception # user not found in DB  
        elif user_from_db.username != SecurityUtilities.decrypt_token_content(decoded_jwt.username):
            raise credentails_exception # user not found in DB  
        else: 
            return usermodels.ltgUserBase(username=user_from_db.username, user_email=user_from_db.user_email)
         
   # build the token data and encode it.  Need to store the token and token data in the DB
    async def encode(self, user_info: usermodels.UserCore, expires_mins: int | None = None) -> str:
        """
        Encodes the user information into a JWT access token.

        Args:
            user_info (usermodels.UserCore): The user information to be encoded.
            expires_mins (int | None, optional): The expiration time of the token in minutes. 
                If not provided, the default expiration time will be used.

        Returns:
            str: The encoded JWT access token.
        """
        if expires_mins is None:
            expires_mins = self.ACCESS_TOKEN_EXPIRE_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_mins)
        # TODO: Break the below TokenData building into a separate function as roles/scope expand
        to_encode = TokenData(
            username=SecurityUtilities.encrypt_token_content(message=user_info.username).decode('utf-8'), 
            roles='', # SecurityUtilities.encrypt_token_content(message=str(user_info.roles)).decode('utf-8'), 
            exp=expire, 
            scope=[])
        encoded_jwt = jwt.encode(to_encode.model_dump(), self.SECRET_KEY, algorithm=self.ALGORITHM)
        # TODO: Need to store the Token and TokenData in a TokenTracker and save to DB here
        # probably in a separate function.
        token = TokenTracker(access_token=encoded_jwt,
                                token_type='bearer',
                                expire_time=int(expire.timestamp()), 
                                user_id=user_info.id, 
                                login_ip='',
        )
        TokenHandler.TOKEN_REPOSITORY.add(token)
        return encoded_jwt


    