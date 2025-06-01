import json
import threading

lock = threading.Lock()

def read_json(filepath):
    with lock:
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

def write_json(filepath, data):
    with lock:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
