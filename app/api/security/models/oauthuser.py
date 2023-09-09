from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Annotated


class User(BaseModel):
    username: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool | None = None


class UserInDB(User):
    hashed_password: str