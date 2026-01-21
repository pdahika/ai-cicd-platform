from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os

security = HTTPBearer()
INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if not INTERNAL_API_KEY:
        raise HTTPException(status_code=500, detail="INTERNAL_API_KEY not set")

    if credentials.credentials != INTERNAL_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
