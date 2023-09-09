from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Annotated

class UserAddress(BaseModel):
    street_1: str
    street_2: str | None = None
    city: str
    state: str
    postal_code: str
    primary: bool = True
    
class DBUserAddress(UserAddress):
    user_id: int