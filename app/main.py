from fastapi import FastAPI
import yfinance as yf
from typing import List, Dict
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def home():
    return {"message": "Stock Analyzer Running"}

@app.get("/top-stocks")
def top_stocks(tickers: str = "RELIANCE.NS,TCS.NS,INFY.NS"):
    """
    Get top stocks based on performance score.
    Args:
        tickers: Comma-separated list of stock symbols
    """
    stocks = [t.strip() for t in tickers.split(",")]
    results = []

    for stock in stocks:
        try:
            data = yf.Ticker(stock).history(period="1mo")

            if data.empty:
                logger.warning(f"No data found for {stock}")
                continue

            latest = data["Close"].iloc[-1]
            avg = data["Close"].mean()

            # Prevent division by zero
            if avg == 0:
                logger.warning(f"Average price is 0 for {stock}")
                continue

            score = (latest - avg) / avg

            results.append({
                "ticker": stock,
                "latest_price": float(latest),
                "avg_price": float(avg),
                "score": float(score),
                "recommendation": "Buy" if score > 0.05 else "Watch"  # 5% threshold
            })

        except Exception as e:
            logger.error(f"Error fetching data for {stock}: {str(e)}")
            continue

    if not results:
        return {"message": "No data available", "results": []}

    return {"results": sorted(results, key=lambda x: x["score"], reverse=True)}