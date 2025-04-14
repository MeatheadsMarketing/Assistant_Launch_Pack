"""
monetization_tags.py – Assistant Launch Pack v1.5

Defines monetization tiers, access plans, or usage models for assistants.
"""

import json
import os

PRICING_CONFIG = "pricing_tiers.json"

def get_pricing_tiers():
    if not os.path.exists(PRICING_CONFIG):
        return {
            "tiers": [
                {"name": "Free", "features": ["Basic GPT tasks"], "price": 0},
                {"name": "Pro", "features": ["All assistants", "Unlimited runs"], "price": 29},
                {"name": "Enterprise", "features": ["Multi-user access", "Priority support"], "price": 99}
            ]
        }
    with open(PRICING_CONFIG, "r") as f:
        return json.load(f)

def save_pricing_tiers(data):
    with open(PRICING_CONFIG, "w") as f:
        json.dump(data, f, indent=2)

# Example usage
if __name__ == "__main__":
    tiers = get_pricing_tiers()
    print(json.dumps(tiers, indent=2))
    save_pricing_tiers(tiers)
