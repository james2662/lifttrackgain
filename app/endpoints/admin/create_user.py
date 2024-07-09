from os import access
from fastapi.responses import JSONResponse
from pydantic import Json
from app.models.usermodels.usermodels import ltgCreateUserReqeust, ltgCreatedUser, UserBase
from dependencies import *
from fastapi.security import OAuth2PasswordRequestForm
from routers.admin import router
from models.security.token import Token
from library.ltgusers.users import LTGUser

@router.post("/create_user", response_model=ltgCreatedUser)
async def create_user(user_data: ltgCreateUserReqeust, 
                current_user: Annotated[UserBase, Depends(LTGUser.get_logged_in_user)]) -> ltgCreatedUser:
    """
    Create a new user
    - **username**: username for the new user
    - **email**: email for the new user
    - **password**: password for the new user
    - **confirm_password**: confirm password for the new user
    """
    
    if user_data.password != user_data.confirm_password:
        return JSONResponse(status_code=409, content={"message": "Passwords do not match"})
    
    if user_data.password == "" or user_data.password is None:
        return JSONResponse(status_code=409, content={"message": "Password cannot be empty"})
    
    if user_data.username == "" or user_data.username is None:
        return JSONResponse(status_code=409, content={"message": "Username cannot be empty"})       
    if user_data.user_email == "" or user_data.user_email is None:    
        return JSONResponse(status_code=409, content={"message": "Email cannot be empty"})
    #  Should I just get user by username and LTGUser or should I use repo and verify unique email and username....
    # TODO: Add check for unique email and username
    if LTGUser.check_user_unique(username=user_data.username, email=user_data.user_email) == False:
        return JSONResponse(status_code=409, content={
            "message": "User would not be suffeciently unique. Please try again."
            }
            )
    

    user = LTGUser.create_user(username=user_data.username, email=user_data.email, password=user_data.password)



    
    return ltgCreatedUser(username=user.username, email=user.useremail, id=user.id)