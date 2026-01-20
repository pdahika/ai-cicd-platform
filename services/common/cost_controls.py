import time
from fastapi import HTTPException

# In real life: Redis or DB, not in-memory
_fix_timestamps = []
_failure_count = 0

MAX_FIXES_PER_HOUR = 5
MAX_FAILURES = 3


def enforce_fix_limits():
    global _fix_timestamps

    now = time.time()
    one_hour_ago = now - 3600

    # Keep only last hour
    _fix_timestamps = [t for t in _fix_timestamps if t > one_hour_ago]

    if len(_fix_timestamps) >= MAX_FIXES_PER_HOUR:
        raise HTTPException(
            status_code=429,
            detail="Fix generation rate limit exceeded. Try later."
        )

    _fix_timestamps.append(now)


def register_failure_and_maybe_block():
    global _failure_count

    _failure_count += 1

    if _failure_count >= MAX_FAILURES:
        raise HTTPException(
            status_code=403,
            detail="Fix generation disabled due to repeated failures."
        )
