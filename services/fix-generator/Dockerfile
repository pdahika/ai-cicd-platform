FROM python:3.10-slim
WORKDIR /app
COPY generator.py .
RUN pip install openai
CMD ["python", "generator.py"]
