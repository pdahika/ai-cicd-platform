FROM python:3.10-slim
WORKDIR /app
COPY analyzer.py .
RUN pip install faiss-cpu sentence-transformers numpy
CMD ["python", "analyzer.py"]
