from os import access
from dependencies import *
from fastapi.security import OAuth2PasswordRequestForm
from endpoints.oauth import router
from models.security.token import Token
from library.ltgusers.users import LTGUser

@router.post("/token", response_model=Token)
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login for access token
    """
    user = LTGUser(form_data.username)
    
    return {"access_token": user.login_user(form_data.password), "token_type": "bearer"}