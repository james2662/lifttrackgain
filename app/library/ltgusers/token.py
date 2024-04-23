
from ..utilities.security import SecurityUtilities
from sqlmodel import Session, SQLModel, select
from jose import JWTError, jwt
from passlib.context import CryptContext
import secrets
from datetime import datetime, timedelta, timezone
from models.usermodels import usermodels
from models.security.token import Token, TokenData


class TokenHandler:
    SECRET_KEY = secrets.token_hex(32)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    def __init__(self):
        
        raise NotImplementedError
    
    async def decode(self, token: Token) -> usermodels.ltgUserBase:
        # TODO: Verify Token, Decode token, and return a ltgUserBase instance
        # verify token

        # Decode Token

        # build and return ltgUserBase instance
        raise NotImplementedError
    
    async def encode(self, user_info: usermodels.ltgUserBase, expires_mins: int | None = None) -> str:
        if expires_mins is None:
            expires_mins = self.ACCESS_TOKEN_EXPIRE_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_mins)
        # TODO: Break the below TokenData buildign into seperate function as roles/scope expand
        to_encode = TokenData(
            username=SecurityUtilities.encrypt_token_content(message=user_info.username).decode('utf-8'), 
            roles=[], 
            exp=expire, 
            scope=[])
        encoded_jwt = jwt.encode(to_encode.model_dump(), self.SECRET_KEY, algorithm=self.ALGORITHM)
        # TODO: Need to store the Token and TokenData in a TokenTracker and save to DB here
        # probably in a seperate function.
        return encoded_jwt
    
    
    