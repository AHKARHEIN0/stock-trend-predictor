import joblib
from pathlib import Path

model_path = Path(__file__).resolve().parents[2] / "app" / "ml" / "predictor_model.pkl"

try:
    model = joblib.load(model_path)
    print("✅ Loaded predictor model.")
except Exception as e:
    print(f"❌ Could not load model: {e}")
    model = None

def predict_action(price, volume):
    if not model:
        print("⚠️ Using fallback 'hold' prediction — model not loaded.")
        return {"action": "hold", "confidence": 0.75}

    input_data = [[price, volume]]

    try:
        prediction = model.predict(input_data)[0]  # "buy", "sell", or "hold"
        confidence = max(model.predict_proba(input_data)[0])  # e.g. 0.91
        return {
            "action": prediction,
            "confidence": round(confidence, 2)
        }
    except Exception as e:
        print(f"❌ Prediction failed: {e}")
        return {"action": "hold", "confidence": 0.75}
