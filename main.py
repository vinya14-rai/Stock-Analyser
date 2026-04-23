from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Stock Analyzer Running"}

@app.get("/top-stocks")
def top_stocks():
    stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

    results = []

    for stock in stocks:
        data = yf.Ticker(stock).history(period="1mo")

        if data.empty:
            continue

        latest = data["Close"].iloc[-1]
        avg = data["Close"].mean()

        score = (latest - avg) / avg

        results.append({
            "ticker": stock,
            "score": float(score),
            "recommendation": "Buy" if score > 0 else "Watch"
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)