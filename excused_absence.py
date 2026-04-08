import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(
    page_title="Excused Absence App",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Excused Absence Management System")

json_path = Path("absence_requests.json")

default_requests = [
    {
        "status": "Pending",
        "course_id": "011101",
        "student_email": "jsmith@university.edu",
        "absence_date": "2026-03-25",
        "submitted_timestamp": "2026-03-19 08:30:00",
        "excuse_type": "Medical",
        "explanation": "I have a scheduled doctor's appointment that I cannot reschedule.",
        "instructor_note": ""
    }
]


if "current_page" not in st.session_state:
    st.session_state["current_page"] = "dashboard"

if "selected_request_index" not in st.session_state:
    st.session_state["selected_request_index"] = None

with st.sidebar:
    st.header("Navigation")

if json_path.exists():
    with open(json_path, "r") as f:
        requests = json.load(f)

student_email = st.text_input("Student Email", key="request_student_email_input")
absence_date = st.date_input("Absence Date", key="request_absence_date_input")
excuse_type = st.selectbox(
    "Excuse Type",
    ["Medical", "University Competitions", "Other"],
    key="request_excuse_type_selectbox"
)
explanation = st.text_area(
    "Student Explanation / Reason",
    key="request_explanation_textarea"
)

if st.button("Submit Request", key="request_submit_button"):
    date_str = absence_date.strftime("%Y-%m-%d")

    new_request = {
        "status": "Pending",
        "course_id": "011101",
        "student_email": student_email,
        "absence_date": date_str,
        "submitted_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "excuse_type": excuse_type,
        "explanation": explanation,
        "instructor_note": ""
    }

    requests.append(new_request)

    with open(json_path, "w") as f:
        json.dump(requests, f, indent=4)

    st.success("Request submitted!")
    st.dataframe(requests)