FROM python:3.10-slim AS builder

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    openai \
    requests

FROM gcr.io/distroless/python3-debian11

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages \
                    /usr/local/lib/python3.10/site-packages

COPY --from=builder /usr/local/bin/python3 \
                    /usr/local/bin/python3

COPY --from=builder /app /app

CMD ["python3", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8002"]
