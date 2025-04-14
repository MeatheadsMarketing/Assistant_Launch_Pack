"""
flow_runner.py – Assistant Launch Pack v1.4

Orchestrates multi-step assistant workflows:
- Step 1: Receive user/system input
- Step 2: Pass through assistant(s)
- Step 3: Optionally write to log, Notion, or webhook
"""

import json
from datetime import datetime

FLOW_LOG_PATH = "flow_log.json"

def run_flow(prompt, steps):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "steps": [],
        "status": "complete"
    }

    for step in steps:
        output = step(prompt)
        log["steps"].append({
            "step_name": step.__name__,
            "output": output
        })
        prompt = output  # pass output to next step

    if not steps:
        log["status"] = "no steps run"

    try:
        if not os.path.exists(FLOW_LOG_PATH):
            with open(FLOW_LOG_PATH, "w") as f:
                json.dump([log], f, indent=2)
        else:
            with open(FLOW_LOG_PATH, "r") as f:
                logs = json.load(f)
            logs.append(log)
            with open(FLOW_LOG_PATH, "w") as f:
                json.dump(logs, f, indent=2)
    except Exception as e:
        print("Error writing flow log:", str(e))

    return log

# Example step functions
def step_echo(prompt):
    return f"Echo: {prompt}"

def step_reverse(prompt):
    return prompt[::-1]

# Test flow (replace with GPT or external APIs later)
if __name__ == "__main__":
    result = run_flow("launch the agent", steps=[step_echo, step_reverse])
    print(json.dumps(result, indent=2))
