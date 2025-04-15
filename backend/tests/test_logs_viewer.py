import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.logs_viewer import read_logs

def test_read_logs_returns_list():
    logs = read_logs()
    assert isinstance(logs, list)
