import streamlit as st
import time
import json
from pathlib import Path

st.set_page_config(
    page_title = "Course Manager",
    page_icon = "",
    layout = "centered",
    initial_sidebar_state = "collapsed"
)

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignments Manager")

next_assignment_id_number = 3

#load assignments
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

json_path = Path("assignments.json")

if json_path.exists():
    with json_path.open("r",encoding="utf=8") as f:
        assignments = json.load(f)

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

with st.sidebar:
    st.markdown("This is a sidebar")
    if st.button("Log out", type="primary",use_container_width=True):
        time.sleep(5)
        st.success("You are being logged out")