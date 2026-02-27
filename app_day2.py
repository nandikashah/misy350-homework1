import streamlit as st

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignments Manager")

next_assignment_id_number = 3

st.divider()

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

import time
import json
from pathlib import Path

json_path = Path("assignments.json")

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