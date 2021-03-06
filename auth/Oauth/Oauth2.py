
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from core.auth.schemas import TokenData
from sqlalchemy.orm import Session
from core.auth.models import User
from core.utils import database_utils


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='v1/auth/login/')



SECRET_KEY= settings.secret_key
ALGORITHM= settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes



def create_access_token(data):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token:str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM)
        id:str= payload.get('user_id')
        if id is None:
            raise credential_exception
        token_data = TokenData(id=id)
            
    except JWTError:
        raise credential_exception
    return token_data



async def get_current_user(token:str =Depends(oauth2_scheme),db:Session = Depends(database_utils.get_db)):
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={'WWW_Authenticate':"Bearer"}
    )
    token= verify_access_token(token, credentials_exception)
    user = db.query(User).filter(User.id == token.id).first()
    return user