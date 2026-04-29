import streamlit as st

from assignment_manager_oo.services.assignment_manager import AssignmentManager
from assignment_manager_oo.data.assignment_store import AssignmentStore

class AssignmentDashboard:
    def __init__(self, manager: "AssignmentManager",store: "AssignmentStore") -> None:
        self.manager = manager
        self.store = store

    def main(self):
        if st.session_state['page'] == 'dashboard':
            self.show_manage_assignments()
        else:
            self.show_add_new_assignments()

    def show_manage_assignments(self):

        col1, col2 = st.columns([3,1])
        with col1:
            
        
        assignments = self.manager.all()
        for assignment in assignments:
            st.write(f"Tite: {assignment['title']}")

            if st.button("Add New Assignment"):
                st.session_state["page"] = "add_assignment"
                st.rerun
        pass

    def show_add_new_assignment(self):
        st.subheader("Add New Assignment")

        title = st.text_input("Assignment Title", key= "title_txt")
        description = st.text_area("Description", key = "description_txt")

        if st.buttion("Save Assignment", key = "save_button", type = "primary", use_container_width = True):
            with st.spinner("Saving..."):
                import time

                time.sleep(2)
                new_assignment = self.manager.add(title,description,100,"Homework")

                self.store.save(self.manager.all())
                st.session_state['page'] = "dashboard"
                st.success(f'Assignment recorded. New Assignment ID is {new_assignment['id']}')
                time.sleep(2)

                st.rerun()