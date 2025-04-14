"""
auth_stub.py – Assistant Launch Pack v1.4

Simple session identity stub. 
Can evolve into full user authentication (OAuth, JWT, etc.)
"""

import streamlit as st
import uuid

def get_user_id():
    if "user_id" not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())
    return st.session_state.user_id

def get_user_label():
    return st.session_state.get("user_label", "anonymous")

def login_widget():
    st.sidebar.markdown("## Login (Stub)")
    user_label = st.sidebar.text_input("Enter your name or tag", value=get_user_label())
    st.session_state.user_label = user_label
    st.sidebar.success(f"Logged in as: {user_label}")

# Example usage
if __name__ == "__main__":
    st.title("Auth Stub Demo")
    login_widget()
    st.write("User ID:", get_user_id())
    st.write("Label:", get_user_label())
