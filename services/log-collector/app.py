import os
import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

class LogPayload(BaseModel):
    pass

@app.post("/logs")
def receive_logs(payload: LogPayload):
    with open("logs.jsonl", "a") as f:
        f.write(json.dumps(payload.dict()) + "\n")

    headers = {"x-api-key": INTERNAL_API_KEY}

    requests.post(
        "http://failure-analyzer:8001/analyze",
        json=payload.dict(),
        headers=headers,
        timeout=5
    )

    return {"message": "log stored + analysis triggered"}
