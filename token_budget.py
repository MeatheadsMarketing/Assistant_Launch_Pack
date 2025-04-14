"""
token_budget.py – Assistant Launch Pack v1.4

Monitors total token usage and alerts or prevents overuse.
"""

import json
from datetime import datetime

TOKEN_LOG = "token_log.json"
BUDGET_LIMIT = 5000  # Example: daily limit

def check_token_budget():
    if not os.path.exists(TOKEN_LOG):
        return {"total": 0, "within_budget": True}

    with open(TOKEN_LOG, "r") as f:
        logs = json.load(f)

    today = datetime.utcnow().date()
    total_tokens_today = sum(
        entry.get("total_tokens", 0)
        for entry in logs
        if datetime.fromisoformat(entry["timestamp"]).date() == today
    )

    return {
        "total": total_tokens_today,
        "within_budget": total_tokens_today <= BUDGET_LIMIT
    }

def report_status():
    status = check_token_budget()
    print(f"Token usage today: {status['total']} / {BUDGET_LIMIT}")
    print("Within budget?" , "✅ Yes" if status['within_budget'] else "❌ No")

if __name__ == "__main__":
    report_status()
