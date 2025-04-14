import streamlit as st
import json
import os
from datetime import datetime

st.title("Assistant Usage Log")

log_file = "shortcut_registry.json"

if os.path.exists(log_file):
    with open(log_file) as f:
        logs = json.load(f)

    st.subheader("Recent Assistant Triggers")
    for entry in reversed(logs[-10:]):
        timestamp = entry.get("timestamp", "unknown")
        shortcut = entry.get("shortcut", "N/A")
        st.markdown(f"• **{shortcut}** triggered at `{timestamp}`")
else:
    st.info("No usage log found.")

# Optional: Add export/download
if os.path.exists(log_file):
    st.download_button("Download Full Log", data=json.dumps(logs, indent=2),
                       file_name="shortcut_registry.json", mime="application/json")
