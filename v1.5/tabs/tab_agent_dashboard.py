import streamlit as st
import json
import os

st.set_page_config(page_title="Agent Dashboard")
st.title("Agent Dashboard")

REGISTRY_PATH = "agent_registry.json"

# Load agent registry
if os.path.exists(REGISTRY_PATH):
    with open(REGISTRY_PATH, "r") as f:
        data = json.load(f)
else:
    st.warning("No agent registry found.")
    data = {"agents": []}

agents = data.get("agents", [])

if agents:
    tags = sorted({tag for agent in agents for tag in agent.get("tags", [])})
    selected_tag = st.sidebar.selectbox("Filter by tag", ["All"] + tags)

    filtered_agents = [
        agent for agent in agents
        if selected_tag == "All" or selected_tag in agent.get("tags", [])
    ]

    for agent in filtered_agents:
        with st.container():
            st.subheader(agent.get("name", "Unnamed Agent"))
            st.markdown(f"**Tags**: {', '.join(agent.get('tags', []))}")
            st.markdown(f"**Status**: `{agent.get('status', 'idle')}`")
            if st.button(f"Launch {agent.get('name', '')}"):
                st.success(f"Triggering {agent.get('name')}...")
else:
    st.info("No agents registered yet.")
