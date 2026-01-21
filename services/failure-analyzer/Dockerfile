FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TRANSFORMERS_CACHE=/tmp/hf_cache

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    faiss-cpu \
    sentence-transformers \
    numpy \
    requests

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001"]
