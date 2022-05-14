from email.policy import default
from sqlalchemy import Column,String,Integer, BOOLEAN, TIMESTAMP
from ..database import Base
from sqlalchemy.sql.expression import text 



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable= False)
    role = Column(String, nullable=False)
    super_user= Column(BOOLEAN, default=False, nullable=False)
    is_verified = Column(BOOLEAN,default=False, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False ,server_default=text('now()'))
    update_at = Column(TIMESTAMP(timezone=True),nullable=True, server_onupdate= text('now()') )
    
    
    