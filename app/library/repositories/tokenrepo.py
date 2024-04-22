from sqlmodel import SQLModel, Session, select
from sqlalchemy.orm.session import Session as SSession
from typing import Any
from abstract.repository import AbstractRepository
from models.security.token import TokenTracker
from sqlalchemy.types import Uuid
from typing import List, Optional
from uuid import UUID as pyUUID
import uuid

class TokenRepository(AbstractRepository):

    def __init__(self, engine_type: str | None = None):
        if engine_type is not None:
            self.new_session(engine_type=engine_type)

    
    def add(self, model: TokenTracker) -> TokenTracker:
        super().add(model=model)
        return model
    
    def get(self, model, reference: str) -> TokenTracker | None:
        statement = select(TokenTracker).where(TokenTracker.access_token == reference)
        result = self.session.exec(statement=statement)
        return result.first()
    
    def update(self, data: TokenTracker) -> TokenTracker:
        super().update(data)
        return data
    
    def remove(self, data: TokenTracker) -> None:
        self.session.delete(data)
        self.session.commit()
        self.session.flush()
        return None