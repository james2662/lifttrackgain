from os import access
from dependencies import *
from fastapi.security import OAuth2PasswordRequestForm
from routers.oauth import router
from models.security.token import Token
from library.ltgusers.users import LTGUser

@router.post("/token")
async def token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    """
    Login for access token
    """
    user = LTGUser(form_data.username)
    
    return user.login_user(form_data.password)