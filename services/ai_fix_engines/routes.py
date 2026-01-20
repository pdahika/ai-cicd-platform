from fastapi import APIRouter, Depends
from services.common.auth import verify_token
from services.ai_fix_engines.service import generate_fix_with_guard

router = APIRouter()


@router.post("/generate-fix")
def generate_fix(payload: dict, _=Depends(verify_token)):
    return generate_fix_with_guard(payload)
