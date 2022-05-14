from ast import Str
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from enum import Enum




class Role(str,Enum):
    learner:str='Learning'
    creator:str= 'Creator'





class TokenData(BaseModel):
    id:Optional[str]=None




class UserBase(BaseModel):

    name: str
    email:EmailStr
    password:str
  
    is_super_user: bool=False



class UserCreate(UserBase):

    role:Role='Learning'
    
    class Config:
        use_enum_values = True

class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
        

class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    role:Role
    created_at:datetime
    
    class Config:
        use_enum_values = True
        orm_mode = True
 
        
class RegistrationUserResponse(BaseModel):
    message:str
    data: UserResponse


class Token(BaseModel):
    access_token:str
    token_type:str
    data: UserResponse
    

class EmailSchema(BaseModel):
    email:EmailStr
    

class PasswordSchema(BaseModel):
    password:str

    
class ResponseConfirmationSchema(BaseModel):
    message:str
    status:bool    
