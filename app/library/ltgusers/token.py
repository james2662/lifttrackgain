
from ..utilities.security import SecurityUtilities
from sqlmodel import Session, SQLModel, select
from models.usermodels import usermodels
from models.security.token import Token, TokenData


class TokenHandler:

    def __init__(self):
        raise NotImplementedError
    
    async def decode(self, token: Token) -> usermodels.ltgUserBase:
        # TODO: Verify Token, Decode token, and return a ltgUserBase instance
        # verify token

        # Decode Token

        # build and return ltgUserBase instance
        raise NotImplementedError
    
    async def encode(self, user_info: usermodels.ltgUserBase) -> Token:
        raise NotImplementedError