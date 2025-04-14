import streamlit as st
import json
import os
from agent_status import get_status

st.set_page_config(page_title="Filter Panel")
st.title("Assistant Filter Panel")

REGISTRY_PATH = "agent_registry.json"

# Load registry
if os.path.exists(REGISTRY_PATH):
    with open(REGISTRY_PATH, "r") as f:
        data = json.load(f)
else:
    st.warning("No agent registry found.")
    data = {"agents": []}

agents = data.get("agents", [])

if not agents:
    st.info("No agents available.")
    st.stop()

# Extract filter options
all_tags = sorted({tag for a in agents for tag in a.get("tags", [])})
all_statuses = sorted(set(get_status(a["name"]) for a in agents))

selected_tag = st.sidebar.selectbox("Filter by Tag", ["All"] + all_tags)
selected_status = st.sidebar.selectbox("Filter by Status", ["All"] + all_statuses)

# Apply filters
filtered = []
for agent in agents:
    name = agent.get("name", "")
    tags = agent.get("tags", [])
    status = get_status(name)

    if (selected_tag == "All" or selected_tag in tags) and        (selected_status == "All" or selected_status == status):
        filtered.append((name, tags, status))

# Display results
st.subheader("Filtered Assistants")
for name, tags, status in filtered:
    st.markdown(f"• **{name}** — `{status}` — *{', '.join(tags)}*")
