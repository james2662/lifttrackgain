from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Annotated

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None