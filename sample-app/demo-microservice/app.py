from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Demo App"

@app.route("/health")
def health():
    if os.getenv("REQUIRED_ENV") is None:
        raise Exception("Missing REQUIRED_ENV")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
