"""
Notion Sync Utility – Assistant Launch Pack v1.3

Syncs feedback log entries or token logs to a Notion database using the Notion API.
"""

import os
import json
import requests
from datetime import datetime

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_DB_ID = os.getenv("NOTION_DB_ID", "your-notion-database-id")
NOTION_TOKEN = os.getenv("NOTION_API_KEY", "your-secret-key")
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def sync_feedback_to_notion(log_path="feedback_log.json"):
    if not os.path.exists(log_path):
        print("No feedback log found.")
        return

    with open(log_path, "r") as f:
        entries = json.load(f)

    for entry in entries[-5:]:  # Sync last 5 entries
        payload = {
            "parent": {"database_id": NOTION_DB_ID},
            "properties": {
                "Timestamp": {"date": {"start": entry["timestamp"]}},
                "Message": {"title": [{"text": {"content": entry["message"]}}]},
                "Tag": {"select": {"name": entry["tag"]}},
                "Source": {"rich_text": [{"text": {"content": entry.get("source", "unknown")}}]}
            }
        }
        response = requests.post(NOTION_API_URL, headers=HEADERS, json=payload)
        if response.status_code != 200:
            print(f"Error syncing entry: {entry['message']}")
            print(response.text)

if __name__ == "__main__":
    sync_feedback_to_notion()
