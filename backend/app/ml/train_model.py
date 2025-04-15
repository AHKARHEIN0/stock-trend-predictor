import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

# Simulated training data
# X = [price, volume]
X = np.array([
    [80, 1500000],   # buy
    [95, 2000000],   # buy
    [150, 700000],   # hold
    [320, 200000],   # sell
    [305, 100000],   # sell
])
y = ["buy", "buy", "hold", "sell", "sell"]

model = RandomForestClassifier()
model.fit(X, y)

Path("backend/app/ml").mkdir(parents=True, exist_ok=True)

from pathlib import Path
model_dir = Path(__file__).resolve().parent
joblib.dump(model, model_dir / "predictor_model.pkl")

print("✅ Model saved.")
