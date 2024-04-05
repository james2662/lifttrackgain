from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

# Schemeas 
class UserBase(SQLModel):
    username: str = Field(index=True, unique=True, nullable=False)
    useremail: str = Field(index=True, nullable=False)
    is_active: bool = Field(default=True)

class UserCore(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
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


