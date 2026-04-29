import streamlit as st
from assignment_manager_oo.services.assignment_manager import AssignmentManager
from assignment_manager_oo.ui.assignment_dashboard import AssignmentDashboard


st.set_page_config("Assignment Manager")

st.title("Assignment Manager")

if "logged_in" not in st.session_state:
    st.session_state['logged_in'] = True

if "role" not in st.session_state:
    st.session_state["role"] = "Instructor"

if st.session_state["logged_in"]:
    if st.session_state["role"] == "Instructor":
        from pathlib import Path
        store = AssignmentStore(Path("assignment_manager_oo/assignments.json")) #create object from the data class and set the object initial state
        manager = AssignmentManager(store.load()) # create an object from the assignment manager class and set the object's initial state
        dashboard = AssignmentDashboard(manager,store) #create an object from the dashboard class and set the object's initial state
        dashboard.main()

    elif st.session_state["role"] == "student":
        pass

else:
    pass
