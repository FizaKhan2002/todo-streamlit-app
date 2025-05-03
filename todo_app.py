import streamlit as st
import json
import os

DATA_FILE = "todo_data.json"

def load_data():
    """Load data from the JSON file, create file if it doesn't exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        # If file doesn't exist, create it with default data structure
        initial_data = {"to_do": [], "completed": []}
        with open(DATA_FILE, "w") as f:
            json.dump(initial_data, f, indent=4)
        return initial_data

def save_data(data):
    """Save data to the JSON file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        st.error(f"Error saving data: {e}")

# Load data into session state
if "data" not in st.session_state:
    st.session_state.data = load_data()

# Title of the app
st.title("📝 To-Do List App")

# Add a new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task.strip():
        st.session_state.data["to_do"].append(new_task.strip())
        save_data(st.session_state.data)
        st.experimental_rerun()
    else:
        st.warning("Task cannot be empty.")

# Display to-do tasks
st.subheader("Your Tasks:")
if st.session_state.data["to_do"]:
    for task in st.session_state.data["to_do"]:
        if st.checkbox(task, key=task):
            st.session_state.data["completed"].append(task)
            st.session_state.data["to_do"].remove(task)
            save_data(st.session_state.data)
            st.experimental_rerun()
else:
    st.write("No tasks yet.")

# Display completed tasks
st.subheader("✅ Completed Tasks:")
if st.session_state.data["completed"]:
    st.write("\\n".join(f"- {task}" for task in st.session_state.data["completed"]))
else:
    st.write("No completed tasks yet.")
