from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy.types import Uuid
from typing import List, Optional
from uuid import UUID as pyUUID
import uuid

# Schemeas 
class UserBase(SQLModel):
    username: str = Field(index=True, unique=True, nullable=False)
    useremail: str = Field(index=True, nullable=False)
    is_active: bool = Field(default=True)

class UserCore(UserBase, table=True):
    id: Optional[pyUUID] = Field(default=Uuid(as_uuid=True), primary_key=True, index=True, default_factory=uuid.uuid4)
    hashed_password: str = Field(nullable=False)

# Response and Request Models
class ltgUserBase(SQLModel):
    username: str
    user_email: str

class ltgCreatedUser(ltgUserBase):
    password: str

class ltgCreateUserReqeust(ltgUserBase):
    password: str
    confirm_password: str


