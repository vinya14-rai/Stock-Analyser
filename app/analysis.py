import yfinance as yf

def get_top_stocks():
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