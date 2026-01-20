from fastapi import FastAPI
from pydantic import BaseModel
from .generator import generate_fix

app = FastAPI()

class FixPayload(BaseModel):
    log: str

@app.post("/generate")
def generate(payload: FixPayload):
    fix = generate_fix(payload.log)
    return {"fix": fix}
