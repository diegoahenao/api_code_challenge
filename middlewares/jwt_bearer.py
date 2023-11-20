from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token
import os

EMAIL_AUTH = os.environ.get("EMAIL_AUTH")

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != EMAIL_AUTH:
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")