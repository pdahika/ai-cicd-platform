from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests

app = FastAPI()

class LogPayload(BaseModel):
    pipeline: str
    status: str
    log: str

@app.post("/logs")
def receive_logs(payload: LogPayload):
    # Store logs locally
    with open("logs.jsonl", "a") as f:
        f.write(json.dumps(payload.dict()) + "\n")

    # Trigger failure analyzer service
    try:
        requests.post(
            "http://failure-analyzer:8001/analyze",
            json=payload.dict(),
            timeout=2
        )
    except Exception as e:
        # Do NOT fail log-collector if analyzer is down
        print(f"[WARN] Failure analyzer not reachable: {e}")

    return {"message": "log stored + analysis triggered"}
