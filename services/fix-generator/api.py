import os
import requests
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel

from generator import generate_fix

INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

if not INTERNAL_API_KEY:
    raise RuntimeError("❌ INTERNAL_API_KEY is not set")

app = FastAPI()

# ---- Auth dependency ----

def verify_token(x_api_key: str = Header(None)):
    if x_api_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return x_api_key

# ---- Request schema ----

class FixPayload(BaseModel):
    log: str

# ---- Endpoint ----

@app.post("/generate")
def generate(payload: FixPayload, auth=Depends(verify_token)):
    fix = generate_fix(payload.log)

    headers = {"x-api-key": INTERNAL_API_KEY}

    requests.post(
        "http://action-executor:8003/execute",
        json=fix,
        headers=headers,
        timeout=5
    )

    return {"status": "fix_sent_to_executor"}
