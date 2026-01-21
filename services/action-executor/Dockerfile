FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    requests \
    gitpython

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8003"]
