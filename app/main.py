from fastapi import FastAPI
from app.db import get_results

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Running"}

@app.get("/top-stocks")
def top_stocks():
    return get_results()