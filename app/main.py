from fastapi import FastAPI
from app.analysis import get_top_stocks

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Stock Analyzer Running"}

@app.get("/top-stocks")
def top_stocks():
    return get_top_stocks()