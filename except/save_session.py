import json
import os
import time

def save_session(code, password):
    save_data = {
        "code": code,
        "password": password,
        "timestamp": time.time()
    }
    if not os.path.exists("save"):
        os.makedirs("save")
    with open(f"save/{code}.json", "w") as f:
        json.dump(save_data, f)

def load_session(code):
    try:
        with open(f"save/{code}.json", "r") as f:
            save_data = json.load(f)
        return save_data
    except FileNotFoundError:
        print(f"세션 코드 {code}가 없습니다.")
        return None
