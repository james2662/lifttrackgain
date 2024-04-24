from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy.types import Uuid
from typing import List, Optional
from uuid import UUID as pyUUID
import uuid


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: str | None = None
    roles: str
    exp: datetime
    scope: List[str]

class TokenTracker(Token, table=True):
    id: Optional[pyUUID] = Field(primary_key=True, index=True, default_factory=uuid.uuid4)
    expire_time: int
    user_id: pyUUID
    login_ip: str