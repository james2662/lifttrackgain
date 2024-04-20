from ..utilities.security import SecurityUtilities
from sqlmodel import Session, SQLModel, select
from models.usermodels import usermodels
from models.security.token import Token, TokenData

class LTGUser:

    def __init__(self, db: Session, username: str):
        # def get_user(db, username: str):

        statement = select(usermodels.UserCore).where(usermodels.UserCore.username == username)
        result = db.exec(statement=statement).first()
        self.core_user = result
        

    def get_user_info(self):
        raise NotImplementedError
    
    def _hash_password(self, plain_test: str) -> str | bytes:
        return SecurityUtilities.get_a2_hash(plain_text=plain_test)
    
    def validate_user(self):
        raise NotImplementedError
    
    def create_user(self):
        raise NotImplementedError
    
    def edit_user(self):
        raise NotImplementedError
    
    def login_user(self):
        raise NotImplementedError

