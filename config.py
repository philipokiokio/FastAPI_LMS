from pydantic import BaseSettings








class Setting(BaseSettings):
    title: str
    database_name:str
    database_host:str
    database_port:str
    database_username:str
    database_password:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:str
    
    
    class Config:
        env_file = '.env'
        


settings  = Setting()