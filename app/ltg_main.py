from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from .library.database import Database

ltg_app = FastAPI(
    title="LiftTrackGainAPI", 
    version="0.1",
    )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db = Database(engine_type='sqllite')

@ltg_app.get("/")
async def get_test():
    return "Hello Tester"

@ltg_app.get("/secret_resource")
async def protected_point(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'token': token}
