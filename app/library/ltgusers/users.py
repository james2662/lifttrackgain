from calendar import c
from ..utilities.security import SecurityUtilities, credentails_exception
from sqlmodel import Session, SQLModel, select
from models.usermodels import usermodels
from models.security.token import Token, TokenData
from library.repositories.usersrepo import UsersRepository
from .token import TokenHandler
from datetime import datetime, timezone

class LTGUser:
    token_handler = TokenHandler()
    user_repo = UsersRepository()
    def __init__(self, username: str, db: Session = None):
        # def get_user(db, username: str):
        try:
            self.user = self.user_repo.get_user_by_username(username=username)
        except Exception as e:
            self.user = None
    def get_user_info(self) -> usermodels.UserCore | None:
        return self.user        
    
    def _hash_password(self, plain_test: str) -> str | bytes:
        return SecurityUtilities.get_a2_hash(plain_text=plain_test)
    
    async def validate_user(self, password: str) -> bool:
        if self.user is None:
            return False
        else:
            return SecurityUtilities.verify_a2_hash(plain_text=password, hashed_text=self.user.hashed_password)
        # we should never get here but fail safe if we do somehow.
        return False
    
    @staticmethod
    def create_user(username: str, email: str, password: str) -> usermodels.UserCore:
        hashed_password = SecurityUtilities.get_a2_hash(plain_text=password)
        # create user in DB
        user = usermodels.UserCore(username=username, useremail=email, hashed_password=hashed_password)
        LTGUser.user_repo.add(model=user)
        return user

        raise NotImplementedError
    
    @staticmethod
    async def get_logged_in_user(token: Token) -> usermodels.UserBase:
        token_data = await LTGUser.token_handler.decode(token=token)
        if token_data.exp < datetime.now(timezone.utc):
            raise credentails_exception
         # build and return ltgUserBase instance
        user_from_db = LTGUser.user_repo.get_user_by_username(SecurityUtilities.decrypt_token_content(token_data.username).decode('utf-8'))  
        if user_from_db is None:
            raise credentails_exception # user not found in DB  
        elif user_from_db.is_active == False:
            raise credentails_exception # user is not active
        else: 
            return usermodels.UserBase(username=user_from_db.username, useremail=user_from_db.user_email)
        
    
    def edit_user(self):
        raise NotImplementedError
    
    async def login_user(self, password: str) -> Token:
        if self.validate_user(password=password):
            userinfo = self.get_user_info()
            if userinfo is None:
                raise credentails_exception
            else:
                encoded_user_info = await self.token_handler.encode(user_info=userinfo)
            return Token(access_token=encoded_user_info, token_type="bearer")
        else:
            raise credentails_exception

