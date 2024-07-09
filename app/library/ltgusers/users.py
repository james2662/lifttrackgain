from calendar import c
from turtle import st
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from ..utilities.security import SecurityUtilities, credentails_exception
from sqlmodel import Session, SQLModel, select
from models.usermodels import usermodels
from models.security.token import Token, TokenData
from library.repositories.usersrepo import UsersRepository
from .token import TokenHandler
from datetime import datetime, timezone
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="oauth/token")

class LTGUser:
    token_handler = TokenHandler()
    user_repo = UsersRepository()
    def __init__(self, username: str, db: Session = None):
        # def get_user(db, username: str):
        try:
            self.user = self.user_repo.get_user_by_username(username=username)
            if self.user is None:
                print(f"User not found: {username} in DB")
        except Exception as e:
            self.user = None
            print(f"Self.user is None: {e}")
        

    def get_user_info(self) -> usermodels.UserCore | None:
        return self.user        
    
    def _hash_password(self, plain_test: str) -> str | bytes:
        return SecurityUtilities.get_a2_hash(plain_text=plain_test)
    
    def validate_user(self, password: str) -> bool:
        if self.user is None:
            return False
        else:
            try:
                print(f"{self.user=}")
                print(f"{type(self.user)=}")
                return SecurityUtilities.verify_a2_hash(plain_text=password, hashed_text=self.user.hashed_password)
            except Exception as e:
                print(f"Error validating user: {e}")
                return False
        # we should never get here but fail safe if we do somehow.
        return False
    
    @staticmethod
    def create_user(username: str, email: str, password: str) -> usermodels.UserCore:
        hashed_password = SecurityUtilities.get_a2_hash(plain_text=password)
        # create user in DB
        user = usermodels.UserCore(username=username, useremail=email, hashed_password=hashed_password)
        print(f"{user=}")
        result = LTGUser.user_repo.add(user)
        print(f"{result=}")
        return user
    
    @staticmethod
    def check_user_unique(username: str, email: str) -> bool:
        result = LTGUser.check_username_exists(username=username)
        if not result:
            result = LTGUser.check_email_exists(email=email)
        return not result
            
    @staticmethod
    def check_username_exists(username: str) -> bool:
        user = LTGUser.user_repo.get_user_by_username(username=username)
        if user is not None:
            return True
        return False
    
    @staticmethod
    def check_email_exists(email: str) -> bool:
        user = LTGUser.user_repo.get_user_by_email(email=email)
        if user is not None:
            return True
        return False
    
    @staticmethod
    def get_logged_in_user(token: Annotated[str, Depends(oauth2_scheme)]) -> usermodels.UserBase:
        token_new = Token(access_token=token, token_type="bearer")
        token_data = LTGUser.token_handler.decode(token=token_new)
        if token_data.exp < datetime.now(timezone.utc).timestamp():
            raise credentails_exception
         # build and return ltgUserBase instance
        user_from_db = LTGUser.user_repo.get_user_by_username(SecurityUtilities.decrypt_token_content(token_data.username).decode('utf-8'))  
        if user_from_db is None:
            raise credentails_exception # user not found in DB  
        elif user_from_db.is_active == False:
            raise credentails_exception # user is not active
        else: 
            return usermodels.UserBase(username=user_from_db.username, useremail=user_from_db.useremail)
        
    
    def edit_user(self):
        raise NotImplementedError
    
    def login_user(self, password: str) -> Token:
        if self.validate_user(password=password):
            if self.user is None:
                raise credentails_exception
            else:
                encoded_user_info = self.token_handler.encode(user_info=self.user)
            return Token(access_token=encoded_user_info, token_type="bearer")
        else:
            raise credentails_exception

