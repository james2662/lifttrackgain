from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routers import oauth
from models.usermodels.usermodels import UserBase
from library.ltgusers.users import LTGUser

from dependencies import *
from library.database import Database



ltg_app = FastAPI()
    #title="LiftTrackGainAPI", 
    #version="0.1",
    
    #)

@ltg_app.get("/")
async def get_test():
    return "Hello Tester"

@ltg_app.get("/secret_resource")
async def protected_point(current_user: Annotated[UserBase, Depends(LTGUser.get_logged_in_user)]):
    return {'current_user': current_user}

ltg_app.include_router(router=oauth.router, prefix="")
