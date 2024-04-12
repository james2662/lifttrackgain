from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from dependencies import *
from library.database import Database

ltg_app = FastAPI(
    title="LiftTrackGainAPI", 
    version="0.1",
    )

@ltg_app.get("/")
async def get_test():
    return "Hello Tester"

@ltg_app.get("/secret_resource")
async def protected_point(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'token': token}
