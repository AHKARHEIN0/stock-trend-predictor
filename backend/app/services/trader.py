from app.services.stock_fetcher import fetch_stock_data
from app.services.risk_manager import is_trade_allowed
from app.services.predictor import predict_action
from app.services.trade_logger import log_trade
from app.services.logs_viewer import get_today_loss
from app.core.config import settings

def simulate_trade_for_symbols(symbols: list[str]):
    print("🚀 simulate_trade_for_symbols() running")

    daily_loss = get_today_loss()
    print(f"📊 Current daily loss: {daily_loss}")

    for symbol in symbols:
        print(f"🔍 Fetching data for {symbol}")
        data = fetch_stock_data(symbol)
        if not data:
            print(f"⚠️ No data for {symbol}")
            continue

        prediction_result = predict_action(data["price"], data["volume"])
        prediction = prediction_result["action"]
        data["confidence"] = prediction_result["confidence"]

        print(f"📈 Prediction for {symbol}: {prediction}")

        if prediction == "hold":
            print(f"⏸️ Holding {symbol} — skipping trade")
            continue

        trade_amount = data["price"] * (settings.MAX_TRADE_PERCENT / 100)
        allowed = is_trade_allowed(data["confidence"], trade_amount, daily_loss)

        print(f"✅ Allowed: {allowed} | Price: {data['price']} | Confidence: {data['confidence']}")

        trade_record = {
            "symbol": symbol,
            "prediction": prediction,
            "allowed": allowed,
            "confidence": data["confidence"],
            "price": data["price"],
            "volume": data["volume"],
        }

        if allowed:
            log_trade(trade_record)
            print(f"📝 Logged trade: {trade_record}")
        else:
            print(f"🚫 Trade blocked by risk filter: {trade_record}")

