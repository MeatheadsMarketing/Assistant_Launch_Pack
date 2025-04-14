"""
Token Usage Tracker – GPT-based token logging for Assistant Launch Pack v1.3
Tracks prompt and completion tokens and logs to token_log.json
"""

import openai
import json
from datetime import datetime
import os

# Optional: Replace with dynamic model selection later
MODEL_NAME = "gpt-4"
token_log_file = "token_log.json"

def track_gpt_tokens(prompt: str, system: str = "", model: str = MODEL_NAME):
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )
        usage = response['usage']
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt,
            "model": model,
            "prompt_tokens": usage["prompt_tokens"],
            "completion_tokens": usage["completion_tokens"],
            "total_tokens": usage["total_tokens"]
        }
        if os.path.exists(token_log_file):
            with open(token_log_file, "r") as f:
                logs = json.load(f)
        else:
            logs = []
        logs.append(entry)
        with open(token_log_file, "w") as f:
            json.dump(logs, f, indent=2)

        return response['choices'][0]['message']['content'], usage

    except Exception as e:
        return f"[Error] {str(e)}", {}

# Example usage (can remove in production):
if __name__ == "__main__":
    output, usage = track_gpt_tokens("How does assistant logging improve product iteration?")
    print("Response:", output)
    print("Usage:", usage)
