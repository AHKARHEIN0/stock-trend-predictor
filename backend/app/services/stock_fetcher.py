import yfinance as yf

def fetch_stock_data(symbol: str):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d", interval="5m")

        if hist.empty:
            return {"error": "No data found for symbol."}

        latest = hist.iloc[-1]
        return {
            "symbol": symbol.upper(),
            "price": round(latest["Close"], 2),
            "volume": int(latest["Volume"])
        }

    except Exception as e:
        return {"error": str(e)}
