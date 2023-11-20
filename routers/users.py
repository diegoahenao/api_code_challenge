from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User
import os

EMAIL_AUTH = os.environ.get("EMAIL_AUTH")
PASS_AUTH = os.environ.get("PASS_AUTH")

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == EMAIL_AUTH and user.password == PASS_AUTH:
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)