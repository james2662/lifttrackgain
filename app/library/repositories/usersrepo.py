from sqlmodel import SQLModel, Session, select
from sqlalchemy.orm.session import Session as SSession
from typing import Any
from library.abstract.repository import AbstractRepository
from models.usermodels.usermodels import UserCore
from sqlalchemy.types import Uuid
from typing import List, Optional
from uuid import UUID as pyUUID
import uuid

class UsersRepository(AbstractRepository):

    def __init__(self, engine_type: str | None = 'sqllite'):
        if engine_type is not None:
            self.session = self.new_session(engine_type=engine_type)
        if engine_type == 'sqllite':
            with self._db.get_scoped_session() as session:
                self.session = session
                
    def add(self, model: UserCore) -> UserCore:
        self.session.add(model)
        self.session.commit()
        self.session.flush()
        return model
    
    def get(self, model, reference: pyUUID) -> UserCore | None:
        return self.session.query(UserCore).where(UserCore.id == reference).first()
    
    def get_user_by_username(self, username: str) -> UserCore | None:
        self.session.commit()
        self.session.flush()
        # statement = select(UserCore).where(UserCore.username == username)
        # result = self.session.execute(statement=statement).first()
        result = self.session.query(UserCore).where(UserCore.username == username).first()
        print(f"result: {result}")
        return result
    
    def get_user_by_name_and_password(self, username: str, password: str) -> UserCore | None:
        statement = select(UserCore).where(UserCore.username == username).where(UserCore.hashed_password == password)
        result = self.session.execute(statement=statement).first()
        return result

    def update(self, data: UserCore) -> UserCore:
        super().update(data)
        return data