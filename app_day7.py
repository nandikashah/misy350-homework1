import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

# Setting page/application identity
st.set_page_config(page_title="Course Manager", layout="centered")
st.title("Course Manager Application")

# Initialize Session State
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user" not in st.session_state:
    st.session_state["user"] = None

if "page" not in st.session_state:
    st.session_state["page"] = "login" 

if "role" not in st.session_state:
    st.session_state["role"] = None 

users = [
    {
         "id": "1",
            "email": "admin@school.edu",
            "full_name": "System Admin",
            "password": "123ssag@43AE",
            "role": "Admin",
            "registered_at": "..."
    }
]

json_path = Path("users.json")
if json_path.exists():
    with open(json_path,"r") as f:
        users = json.load(f)

assignments = [
    {
        "id" : "HW1",
        "title" : "Introduction to Database",
        "description" : "bascis of database design",
        "points" : 100,
        "type" : "homework"
    },
    {
        "id" : "HW2",
        "title" : "Normalization",
        "description" : "normalize the table designs",
        "points" : 100,
        "type" : "lab"
    }
]


if st.session_state["role"] == "Admin":
    st.markdown("This is the Admin UI-Dashboard")

    if st.button("Log Out"):
        with st.spinner("logging out..."):
            time.sleep(4)
            st.session_state["logged_in"] = False
            st.session_state["user"] = None
            st.session_state["role"] = None
            st.rerun()

elif st.session_state["role"] == "Instructor":
    #st.markdown("This is the Instructor Dashboard")
    if st.session_state["page"] == "home":
        st.markdown(f"Welcome {st.session_state['user']['email']}")
        if st.button("Go to Dashboard", type = "primary", key="view_dash_btn"):
            st.session_state["page"] = 'dashboard'
            st.rerun()
    elif st.session_state["page"] == "dashboard":
        tab1, tab2, tab3 = st.tabs(["View Assignments", "Add New Assignment", "Update an Assignment"])

        with tab1:
            #st.info("This tab is under development")
            option = st.radio("View/Search",["View","Search"],horizontal = True)
            if option == "View":
                st.dataframe(assignments)

            else:
                #search_title = st.selectbox("Assignment Titles", [])
                titles = []
                for assignment in assignments:
                    titles.append(assignment["title"])

                if not titles:
                    st.warning("No assignment is found")
                else:
                    selected_title = st.selectbox("Assignment Title",titles)

                    for assignment in assignments:
                        if assignment["title"] == selected_title:
                            with st.expander("Assignment Details", expanded=True):
                                st.markdown(f"### Title: {assignment['title']}")
                                st.markdown(f"Description: {assignment['description']}")
                                st.markdown(f"Type: **{assignment['type']}**")
                            break
                    selected_assignment = st.selectbox('Assignment Title',
                                                    options = assignments,
                                                    format_func = lambda x: f"{x['title']}",
                                                    key = "new_assignment")
                    with st.expander("Assignment Details", expanded=True):
                                st.markdown(f"### Title: {assignment['title']}")
                                st.markdown(f"Description: {assignment['description']}")
                                st.markdown(f"Type: **{assignment['type']}**")
                    

        with tab2:
            #add new assignment
            st.markdown("### Add New Assignment")

            #INPUT
            title = st.text_input("Title",placeholder="ex: Homework 1",
                                help="This is the name of the assignment")

            #if you use "" instead of "Title", it'll remove the smaller grey title

            description = st.text_area("Description",placeholder="ex: Database Design...")
            due_date = st.date_input("Due Date")
            assignments_type = st.radio("Type",["Homework","Lab"])

            points = st.number_input("Points")


            #assignments_type2 = st.selectbox("Type",["Homework","Lab","Other"])
            #if assignments_type2 == "Other":
            #   assignments_type2 = st.text_input("Assignment Type")

            #lab = st.checkbox("Lab")

            with st.expander("Assignment Preview"):
                st.markdown("## Live Preview")
                st.markdown(f"Title: {title}")

            btn_save = st.button("Save", use_container_width=True, disabled=False)


            if btn_save:
                #st.warning("Working on it!")
                with st.spinner("Saving the assignment..."):
                    time.sleep(5)
                    if not title:
                        st.warning("Enter Assignment Title")

                    else:
                        new_assignment_id = "HW" + str(next_assignment_id_number)
                        next_assignment_id_number += 1

                        assignments.append(
                            {
                                "id": new_assignment_id,
                                "title": title,
                                "description": description,
                                    "points": points,
                                    "type": assignments_type
                            }
                        )
                        
                        #Recording the data into an actual file
                        #if json_path.exists():
                        with json_path.open("w",encoding="utf-8") as f:
                            json.dump(assignments,f)


                        st.success("Assignment is recorded!")
                        st.dataframe(assignments)


                    st.success("Assignment is recorded!")

        
        with tab3: 
            st.markdown("### Update an Assignment")

            titles = []
            for assignment in assignments:
                titles.append(assignment["title"])

            selected_item = st.selectbox("Select an item", titles,key = "search_titles")
            
            selected_assignment = {}
            for assignment in assignments:
                if assignment["title"] == selected_item:
                    selected_assignment = assignment
                    break

            edit_title = st.text_input("Title", value = selected_assignment["title"], key = f"edit_title_{selected_assignment["id"]}")
            edit_description = st.text_area("Description", value = selected_assignment['description'],
                                            key = f"edit_description_{selected_assignment['id']}")
            
            type_list = ["homework","Lab"]
            selected_assignment_type_index = type_list.index(selected_assignment['type'])

            edit_type = st.radio('Type', type_list, index = selected_assignment_type_index,
                                key = f"edit_type_{selected_assignment['id']}")


            update_btn = st.button("Update Assignment", key = "btn_update", use_container_width = True, type = "primary")
            if update_btn:
                with st.spinner("Updating the assignment..."):
                    time.sleep(5)
                    selected_assignment['title'] = edit_title
                    selected_assignment['description'] = edit_description

                    with json_path.open("w", encoding = "utf-8") as f:
                        json.dump(assignments,f)

                    st.success("Assignment is updated!")
                    time.sleep(5)
                    st.rerun()

                
                    #st.dataframe(assignments)


else:
    # --- LOGIN ---
    st.subheader("Log In")
    with st.container(border=True):
        email_input = st.text_input("Email", key="login_email")
        password_input = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Log In", type = "primary", use_container_width = True):
            with st.spinner("Logging in..."):
                time.sleep(2) # Fake backend delay
                
                # Find user
                found_user = None
                for user in users:
                    if user["email"].strip().lower() == email_input.strip().lower() and user["password"] == password_input:
                        found_user = user
                        break
                
                if found_user:
                    st.success(f"Welcome back, {found_user['email']}!")
                    st.session_state["logged_in"] = True
                    st.session_state["user"] = found_user
                    st.session_state["role"] = found_user['role']
                    st.session_state["page"] = "home"
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    # --- REGISTRATION ---
    st.subheader("New Instructor Account")
    with st.container(border=True):
        new_email = st.text_input("Email Address", key="reg_email")
        new_password = st.text_input("Password", type="password", key="reg_password")
        
        if st.button("Create Account"):
            with st.spinner("Creating account..."):
                time.sleep(2) # Fake backend delay
                # ... (Assume validation logic here) ...
                users.append({
                    "id": str(uuid.uuid4()),
                    "email": new_email,
                    "password": new_password,
                    "role": "Instructor"
                })
                with open(json_file, "w") as f:
                    json.dump(users, f, indent=4)
                st.success(f"Account created! {new_email}")
                time.sleep(4)
                st.rerun()

    st.write("---")
    st.dataframe(users)

with st.sidebar:
    if "logged_in" in st.session_state and st.session_state["logged_in"] != False:
        user = st.session_state["user"]
        st.markdown(f" Welcome {user['email']}")
    else:
        st.markdown("Welcome! - Login")
