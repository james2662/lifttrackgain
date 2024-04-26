from fastapi.responses import JSONResponse
from ..utilities.security import SecurityUtilities, credentails_exception
from sqlmodel import Session, SQLModel, select
from jose import JWTError, jwt
from passlib.context import CryptContext
import secrets
from datetime import datetime, timedelta, timezone
from models.usermodels import usermodels
from models.security.token import Token, TokenData
import os




class TokenHandler:
    SECRET_KEY: str = secrets.token_hex(32)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    def __init__(self):
        meaning_of_life = os.environ.get('ltg_life_meaning')
        if meaning_of_life is not None:
            TokenHandler.SECRET_KEY = meaning_of_life
        else:
            os.environ['ltg_life_meaning'] = TokenHandler.SECRET_KEY
        raise NotImplementedError
    
    async def decode(self, token: Token) -> usermodels.ltgUserBase:
        # TODO: Verify Token, Decode token, and return a ltgUserBase instance
        # verify token
        if token is None or  token.access_token is None:
            raise credentails_exception # no token  
        
        # Decode Token
        try:
            decoded_jwt = TokenData.model_construct(
                **jwt.decode(token.access_token, self.SECRET_KEY, algorithms=[self.ALGORITHM]))
        except JWTError:
            raise credentails_exception

        # build and return ltgUserBase instance
        raise NotImplementedError
    
    async def encode(self, user_info: usermodels.ltgUserBase, expires_mins: int | None = None) -> str:
        if expires_mins is None:
            expires_mins = self.ACCESS_TOKEN_EXPIRE_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_mins)
        # TODO: Break the below TokenData buildign into seperate function as roles/scope expand
        to_encode = TokenData(
            username=SecurityUtilities.encrypt_token_content(message=user_info.username).decode('utf-8'), 
            roles='', # SecurityUtilities.encrypt_token_content(message=str(user_info.roles)).decode('utf-8'), 
            exp=expire, 
            scope=[])
        encoded_jwt = jwt.encode(to_encode.model_dump(), self.SECRET_KEY, algorithm=self.ALGORITHM)
        # TODO: Need to store the Token and TokenData in a TokenTracker and save to DB here
        # probably in a seperate function.
        return encoded_jwt
    

    