import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('timetable.db')

# Function to add a professor
def add_professor(name, specialization):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO professors (name, specialization) VALUES (?, ?)", (name, specialization))
    conn.commit()
    conn.close()

# Function to add a subject
def add_subject(name, department, professor_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO subjects (name, department, professor_id) VALUES (?, ?, ?)", (name, department, professor_id))
    conn.commit()
    conn.close()

# Function to add time slots
def add_time_slot(day, start_time, end_time):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO time_slots (day, start_time, end_time) VALUES (?, ?, ?)", (day, start_time, end_time))
    conn.commit()
    conn.close()

# Function to get all professors
def get_professors():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM professors", conn)
    conn.close()
    return df

# Function to get all subjects
def get_subjects():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM subjects", conn)
    conn.close()
    return df

# Function to get all time slots
def get_time_slots():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM time_slots", conn)
    conn.close()
    return df

# Function to generate the timetable based on available slots and professors
def generate_timetable(university_start_date, university_end_date):
    subjects = get_subjects()
    time_slots = get_time_slots()

    timetable = []
    
    # Generate the timetable
    for _, slot in time_slots.iterrows():
        day = slot['day']
        start_time = slot['start_time']
        end_time = slot['end_time']
        
        for _, subject in subjects.iterrows():
            professor_id = subject['professor_id']
            subject_name = subject['name']
            department = subject['department']
            professor_name = get_professors().loc[get_professors()['id'] == professor_id, 'name'].values[0] if professor_id else "N/A"
            
            # Create a timetable entry
            timetable.append({
                "Day": day,
                "Time": f"{start_time} - {end_time}",
                "Subject": subject_name,
                "Department": department,
                "Professor": professor_name
            })

    return pd.DataFrame(timetable)

# Streamlit UI
st.title("AI-Based Timetable Generator")

# University Dates Input
st.header("University Schedule")
university_start_date = st.date_input("University Start Date", datetime.today())
university_end_date = st.date_input("University End Date", datetime.today() + timedelta(days=180))

# Add Professor
st.header("Add Professor")
with st.form(key='professor_form'):
    name = st.text_input("Professor Name")
    specialization = st.text_input("Specialization")
    submit_professor = st.form_submit_button("Add Professor")
    if submit_professor:
        add_professor(name, specialization)
        st.success(f"Professor {name} added successfully!")

# Add Subject
st.header("Add Subject")
with st.form(key='subject_form'):
    subject_name = st.text_input("Subject Name")
    department = st.text_input("Department")
    professors = get_professors()
    professor_id = st.selectbox("Select Professor", [None] + professors['id'].tolist())
    submit_subject = st.form_submit_button("Add Subject")
    if submit_subject:
        add_subject(subject_name, department, professor_id)
        st.success(f"Subject {subject_name} added successfully!")

# Add Time Slot
st.header("Add Time Slot")
with st.form(key='time_slot_form'):
    day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    start_time = st.time_input("Start Time", value=datetime.strptime("09:00", "%H:%M").time())
    end_time = st.time_input("End Time", value=datetime.strptime("10:00", "%H:%M").time())
    submit_time_slot = st.form_submit_button("Add Time Slot")
    if submit_time_slot:
        add_time_slot(day, str(start_time), str(end_time))
        st.success(f"Time Slot for {day} added successfully!")

# Generate Timetable
if st.button("Generate Timetable"):
    timetable = generate_timetable(university_start_date, university_end_date)
    st.write("Generated Timetable:")
    st.dataframe(timetable)

    # Download timetable as CSV
    csv = timetable.to_csv(index=False).encode('utf-8')
    st.download_button("Download Timetable", csv, "timetable.csv", "text/csv")
