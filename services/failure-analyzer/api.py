from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import find_similar

app = FastAPI()

class FailurePayload(BaseModel):
    pipeline: str
    status: str
    log: str

@app.post("/analyze")
def analyze(payload: FailurePayload):
    match = find_similar(payload.log)

    if match:
        return {"action": "known_fix", "fix": match}

    return {"action": "generate_fix"}
