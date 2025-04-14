import streamlit as st
import json
import os

st.title("System Audit & Version Snapshot")

# Load version manifest
if os.path.exists("version_manifest.json"):
    with open("version_manifest.json") as f:
        manifest = json.load(f)
    st.subheader("Version Manifest")
    st.json(manifest)
else:
    st.warning("No version_manifest.json found.")

# Show audit results if available
if os.path.exists("v1.3_dev_audit.json"):
    with open("v1.3_dev_audit.json") as f:
        audit = json.load(f)
    st.subheader("Audit Log (v1.3-dev)")
    for entry in audit:
        st.markdown(f"`{entry['file']}` | {entry['status']} | {entry['exec_status']}")
else:
    st.info("No audit log available.")

# Optional: Link other logs (feedback, tokens)
if os.path.exists("feedback_log.json"):
    with open("feedback_log.json") as f:
        feedback = json.load(f)
    st.subheader("Feedback Log (last 3)")
    for entry in reversed(feedback[-3:]):
        st.write(f"[{entry['timestamp']}] ({entry['tag']}) – {entry['message']}")

if os.path.exists("token_log.json"):
    with open("token_log.json") as f:
        tokens = json.load(f)
    st.subheader("Token Usage Log (last 3)")
    for entry in reversed(tokens[-3:]):
        st.write(f"[{entry['timestamp']}] {entry['total_tokens']} tokens used")
