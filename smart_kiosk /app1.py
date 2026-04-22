import streamlit as st

st.set_page_config("Assignment Manager")

st.title("Assignment Manager")

if "logged_in" not in st.session_state:
    st.session_state['logged_in'] = True

if "role" not in st.session_state:
    st.session_state["role"] = "Instructor"

