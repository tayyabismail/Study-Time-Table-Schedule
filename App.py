import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Title
st.title("Student Daily Timetable Maker")

# Input form for timetable
st.header("Create Your Daily Timetable")

# Get start time of the day
start_time = st.time_input("Start Time", value=datetime.strptime("08:00", "%H:%M").time())

# Number of tasks
num_tasks = st.number_input("How many tasks do you want to add?", min_value=1, step=1)

# List to store tasks and their durations
tasks = []
durations = []

for i in range(num_tasks):
    task = st.text_input(f"Task {i+1} Name", f"Task {i+1}")
    duration = st.number_input(f"Duration for Task {i+1} (in hours)", min_value=0.25, step=0.25)
    tasks.append(task)
    durations.append(duration)

# Generate the timetable
if st.button("Generate Timetable"):
    st.subheader("Your Timetable for the Day")

    # Create timetable
    timetable = []
    current_time = datetime.combine(datetime.today(), start_time)

    for i in range(num_tasks):
        end_time = current_time + timedelta(hours=durations[i])
        timetable.append({
            "Task": tasks[i],
            "Start Time": current_time.strftime("%I:%M %p"),
            "End Time": end_time.strftime("%I:%M %p")
        })
        current_time = end_time

    # Display timetable as a DataFrame
    df = pd.DataFrame(timetable)
    st.dataframe(df)

# Footer
st.write("Plan your day wisely and stay productive!")
