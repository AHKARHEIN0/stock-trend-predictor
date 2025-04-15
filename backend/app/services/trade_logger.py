import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("backend/logs/trade_log.json")

def log_trade(data: dict):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    data["timestamp"] = datetime.utcnow().isoformat()
    
    if LOG_FILE.exists():
        existing = json.loads(LOG_FILE.read_text())
    else:
        existing = []

    existing.append(data)
    LOG_FILE.write_text(json.dumps(existing, indent=2))
