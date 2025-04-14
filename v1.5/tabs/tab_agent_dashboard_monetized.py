import streamlit as st
import json
import os
from agent_status import get_status, set_status

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
    tiers = sorted({agent.get("tier", "Free") for agent in agents})

    selected_tag = st.sidebar.selectbox("Filter by tag", ["All"] + tags)
    selected_tier = st.sidebar.selectbox("Filter by tier", ["All"] + tiers)

    filtered_agents = [
        agent for agent in agents
        if (selected_tag == "All" or selected_tag in agent.get("tags", []))
        and (selected_tier == "All" or selected_tier == agent.get("tier", "Free"))
    ]

    for agent in filtered_agents:
        name = agent.get("name", "Unnamed Agent")
        tier = agent.get("tier", "Free")
        with st.container():
            st.subheader(name)
            st.markdown(f"**Tags**: {', '.join(agent.get('tags', []))}")
            st.markdown(f"**Tier**: `{tier}`")
            current_status = get_status(name)
            st.markdown(f"**Status**: `{current_status}`")

            col1, col2 = st.columns(2)
            if col1.button(f"Set {name} to Running"):
                set_status(name, "running")
                st.experimental_rerun()
            if col2.button(f"Set {name} to Idle"):
                set_status(name, "idle")
                st.experimental_rerun()
else:
    st.info("No agents registered yet.")
