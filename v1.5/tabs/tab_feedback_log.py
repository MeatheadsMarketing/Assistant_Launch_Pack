import streamlit as st
import json
from datetime import datetime
import os

st.title("Feedback Log")

feedback_file = "feedback_log.json"
default_tags = ["info", "idea", "issue", "note"]

with st.form("feedback_form"):
    message = st.text_area("Your Feedback")
    tag = st.selectbox("Type", default_tags)
    submit = st.form_submit_button("Submit")

if submit and message:
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": message,
        "tag": tag,
        "source": "user"
    }
    if os.path.exists(feedback_file):
        with open(feedback_file, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(entry)
    with open(feedback_file, "w") as f:
        json.dump(data, f, indent=2)
    st.success("Feedback submitted.")

# Display current log entries
if os.path.exists(feedback_file):
    st.markdown("### Logged Feedback")
    with open(feedback_file, "r") as f:
        feedback_entries = json.load(f)
    for entry in reversed(feedback_entries[-5:]):
        st.write(f"[{entry['timestamp']}] ({entry['tag']}) – {entry['message']}")
