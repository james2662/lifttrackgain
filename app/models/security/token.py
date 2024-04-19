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
    roles: List[str]
    expire_time: int
    scope: List[str]

class TokenTracker(Token, table=True):
    expire_time: int
    user_id: pyUUID
    login_ip: str