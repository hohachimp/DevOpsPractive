import os
from fastapi import FastAPI

app = FastAPI()
MESSAGE = os.getenv("APP_MESSAGE", "Hello from Lucas!")

@app.get("/")
def home():
    return {"message": MESSAGE}

@app.get("/health-check")
def health():
    return {"status": "ok"}
