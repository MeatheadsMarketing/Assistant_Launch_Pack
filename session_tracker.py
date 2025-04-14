"""
session_tracker.py – Assistant Launch Pack v1.4

Tracks user sessions and assistant interaction history.
Useful for:
- Usage auditing
- Multi-user systems
- Replay/debug logs
"""

import json
import uuid
import os
from datetime import datetime

SESSION_LOG = "session_log.json"

def new_session(user="anonymous"):
    session_id = str(uuid.uuid4())
    entry = {
        "session_id": session_id,
        "user": user,
        "start_time": datetime.utcnow().isoformat(),
        "actions": []
    }
    append_session_log(entry)
    return session_id

def log_action(session_id, action_type, details=""):
    try:
        if os.path.exists(SESSION_LOG):
            with open(SESSION_LOG, "r") as f:
                data = json.load(f)
        else:
            data = []

        for entry in data:
            if entry["session_id"] == session_id:
                entry["actions"].append({
                    "timestamp": datetime.utcnow().isoformat(),
                    "type": action_type,
                    "details": details
                })
                break

        with open(SESSION_LOG, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print("Session log error:", str(e))

def append_session_log(entry):
    if os.path.exists(SESSION_LOG):
        with open(SESSION_LOG, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(entry)
    with open(SESSION_LOG, "w") as f:
        json.dump(data, f, indent=2)

# Example usage
if __name__ == "__main__":
    sid = new_session("test_user")
    log_action(sid, "feedback", "Submitted test feedback.")
