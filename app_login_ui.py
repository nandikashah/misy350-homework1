import streamlit as st
from pathlib import Path
import datetime
import uuid
import json
import time

st.set_page_config(
    page_title = "Course Manager",
    page_icon = "",
    layout = "centered",
    initial_sidebar_state = "collapsed")

st.title("Course Manager")

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

json_file = Path("users.json")
if json_file.exists():
    with json_file.open("r",encoding="utf=8") as f:
        users = json.load(f)
    


next_user_id_number = 2

tab1, tab2, tab3 = st.tabs(["Register", "Login", "Critical Verification"])

with tab1:
    st.container(border = True)
    st.markdown("### New Instructor Account")
    full_name = st.text_input("First and Last Name",placeholder="Jane Doe")
    email = st.text_input("Email Address",placeholder="janedoe@udel.edu",help="use udel.edu")
    password = st.text_input("Password",type="password")
    role = st.selectbox("Role",["Instructor","Other"])

    
    create_acct_button = st.button("Create Account", use_container_width=True, disabled=False)

    if create_acct_button:
        #st.warning("Working on it!")
        with st.spinner("Creating your account..."):
            time.sleep(5)
            if not full_name and not email and not password:
                st.warning("Please complete empty fields")

            else:
                new_user_id = next_user_id_number
                next_user_id_number += 1
                
                users.append(
                    {
                        "id": new_user_id,
                        "email": email,
                        "full_name": full_name,
                        "password": password,
                        "role": role
                    }
                )
                
                #Recording the data into an actual file
                #if json_path.exists():
                with json_file.open("w",encoding="utf-8") as f:
                    json.dump(users,f)


                st.success("Account created successfully!")
                st.dataframe(users)


            st.success("Account created successfully!")
