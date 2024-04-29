from sqlmodel import SQLModel, Session, select
from sqlalchemy.orm.session import Session as SSession
from typing import Any
from abstract.repository import AbstractRepository
from models.usermodels.usermodels import UserCore
from sqlalchemy.types import Uuid
from typing import List, Optional
from uuid import UUID as pyUUID
import uuid

class UsersRepository(AbstractRepository):

    def __init__(self, engine_type: str | None = None):
        if engine_type is not None:
            self.new_session(engine_type=engine_type)

    
    def add(self, model: UserCore) -> UserCore:
        super().add(model=model)
        return model
    
    def get(self, model, reference: pyUUID) -> UserCore:
        return super().get(model=UserCore, reference=reference)
    
    def get_user_by_username(self, username: str) -> UserCore:
        statement = select(UserCore).where(UserCore.username == username)
        result = self.session.exec(statement=statement).first()
        return result
    
    def get_user_by_name_and_password(self, username: str, password: str) -> UserCore:
        statement = select(UserCore).where(UserCore.username == username).where(UserCore.hashed_password == password)
        result = self.session.exec(statement=statement).first()
        return result

    def update(self, data: UserCore) -> UserCore:
        super().update(data)
        return data