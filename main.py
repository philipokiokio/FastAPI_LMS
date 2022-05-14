from fastapi import FastAPI

from core.config import settings
from core.auth import auth_router



app = FastAPI(title=settings.title)


app.include_router(auth_router.auth)

@app.get('/')
def root():
    return {
        "welcome to ": "I am the Server",
        "docs":"/docs"
    }