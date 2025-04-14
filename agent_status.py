"""
agent_status.py – Assistant Launch Pack v1.5

Reads and updates agent status (idle, running, failed).
"""

import json
import os

STATUS_FILE = "agent_status.json"

def load_status():
    if not os.path.exists(STATUS_FILE):
        return {}
    with open(STATUS_FILE, "r") as f:
        return json.load(f)

def save_status(data):
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_status(agent_name):
    status_map = load_status()
    return status_map.get(agent_name, "idle")

def set_status(agent_name, status):
    status_map = load_status()
    status_map[agent_name] = status
    save_status(status_map)

# Example usage
if __name__ == "__main__":
    print("Setting status...")
    set_status("SEO Analyzer", "running")
    print("Current status:", get_status("SEO Analyzer"))
