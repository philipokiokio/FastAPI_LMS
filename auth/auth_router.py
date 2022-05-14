from fastapi import APIRouter,Depends,HTTPException,status
from . import schemas
from sqlalchemy.orm import Session
from core.utils import database_utils
from .Oauth.Oauth2 import get_current_user, create_access_token
from .models import User
from .Oauth.oauth_utils import oauth_utils



auth = APIRouter(tags=['Authentication'], prefix='/v1/auth')



@auth.post('/register', status_code=status.HTTP_201_CREATED, response_model=schemas.RegistrationUserResponse)
def user_register(user_data:schemas.UserCreate, db:Session=Depends(database_utils.get_db)):
    
    
    db_user_data = User(**user_data.dict)
    db_user_data.password = oauth_utils.get_password_hashed(db_user_data.password)
    db.add(db_user_data)
    db.commit()
    db.refresh(db_user_data)
    
    return {
        "message": "User Regsitered Sucessfully.",
        "data":db_user_data
    }