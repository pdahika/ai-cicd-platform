import requests
import os
from similarity import find_similar
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from pydantic import BaseModel

app = FastAPI()
security = HTTPBearer()

class FailurePayload(BaseModel):
    log: str

def verify_token(credentials: HTTPAuthCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("API_TOKEN"):
        raise ValueError("Invalid token")
    return token

INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

@app.post("/analyze")
def analyze(payload: FailurePayload, auth=Depends(verify_token)):
    match = find_similar(payload.log)

    headers = {"x-api-key": INTERNAL_API_KEY}

    if match:
        requests.post(
            "http://action-executor:8003/execute",
            json=match,
            headers=headers
        )
        return {"action": "known_fix_applied"}

    requests.post(
        "http://fix-generator:8002/generate",
        json={"log": payload.log},
        headers=headers
    )

    return {"action": "fix_generation_triggered"}

