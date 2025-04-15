import json
import random
from datetime import datetime, timezone
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent.parent.parent / "logs" / "trade_log.json"

def log_trade(data: dict):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    data["timestamp"] = datetime.now(timezone.utc).isoformat()

    # Simulate a fake win/loss outcome
    data["result"] = random.choice(["win", "loss"])

    if LOG_FILE.exists():
        existing = json.loads(LOG_FILE.read_text())
    else:
        existing = []

    existing.append(data)
    LOG_FILE.write_text(json.dumps(existing, indent=2))

