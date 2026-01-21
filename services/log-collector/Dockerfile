FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    pydantic \
    requests

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]
