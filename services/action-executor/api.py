from fastapi import FastAPI, Depends
from pydantic import BaseModel
from executor import apply_patch
from common.auth import verify_token

app = FastAPI()

class FixPayload(BaseModel):
    file: str
    change: str
    reason: str

@app.post("/execute")
def execute_fix(payload: FixPayload, auth=Depends(verify_token)):
    apply_patch(payload.file, payload.change)
    return {"status": "patch_applied"}
