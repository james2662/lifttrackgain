
from ..utilities.security import SecurityUtilities
from sqlmodel import Session, SQLModel, select
from models.usermodels import usermodels
from models.security.token import Token, TokenData


class TokenHandler:

    def __init__(self):
        raise NotImplementedError
    
    def decode(self):
        raise NotImplementedError
    
    def encode(self):
        raise NotImplementedError