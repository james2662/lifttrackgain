from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from library.database import Database


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db(engine_type: str | None):
    return Database(session=None, envrionment=None, engine_type='sqllite')

db = get_db('sqllite')