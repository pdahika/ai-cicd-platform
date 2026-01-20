from services.common.cost_controls import (
    enforce_fix_limits,
    register_failure_and_maybe_block
)

from services.ai_fix_engine.llm import generate_fix


def generate_fix_with_guard(issue_payload: dict):
    # 🚦 Cost + abuse control
    enforce_fix_limits()

    try:
        fix = generate_fix(issue_payload)
        return fix

    except Exception as e:
        # ❌ Count failures to block abuse or bad loops
        register_failure_and_maybe_block()
        raise e
