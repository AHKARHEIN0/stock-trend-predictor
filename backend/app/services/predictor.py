import joblib
from pathlib import Path

model_path = Path("backend/app/ml/predictor_model.pkl")

try:
    model = joblib.load(model_path)
except:
    model = None

def predict_action(price: float, volume: int) -> str:
    if model:
        try:
            prediction = model.predict([[price, volume]])
            return prediction[0]
        except Exception as e:
            print("Model failed, fallback:", e)

    # fallback rule-based
    if price < 100 and volume > 1_000_000:
        return "buy"
    elif price > 300 and volume < 500_000:
        return "sell"
    else:
        return "hold"
