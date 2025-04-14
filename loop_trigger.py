"""
loop_trigger.py – Assistant Launch Pack v1.4

Runs assistant workflows on a repeat interval or until a stop condition is met.
Useful for:
- Auto-running research agents
- Polling and auto-loggers
- Background GPT task loops
"""

import time
from flow_runner import run_flow, step_echo, step_reverse

LOOP_LOG = "loop_run_log.json"

def loop_execute(prompt, steps, interval_sec=60, max_loops=3):
    runs = []
    for i in range(max_loops):
        print(f"Loop {i+1}/{max_loops}")
        result = run_flow(prompt, steps)
        runs.append(result)
        with open(LOOP_LOG, "w") as f:
            import json
            json.dump(runs, f, indent=2)
        time.sleep(interval_sec)

    return runs

# Example loop with simple echo/reverse steps
if __name__ == "__main__":
    loop_execute("autonomous test run", steps=[step_echo, step_reverse], interval_sec=3, max_loops=2)
