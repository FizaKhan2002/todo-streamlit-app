import streamlit as st
import json
import os
# Initialize session state
if "to_do" not in st.session_state:
    st.session_state.to_do = []

if "completed" not in st.session_state:
    st.session_state.completed = []

st.title("📝 To-Do List App")

# Add new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task.strip():
        st.session_state.to_do.append(new_task.strip())
        st.success(f"Added: {new_task.strip()}")
    else:
        st.warning("Task cannot be empty.")

# Display tasks
st.subheader("Your Tasks:")
if st.session_state.to_do:
    remove_tasks = []
    for i, task in enumerate(st.session_state.to_do):
        if st.checkbox(task, key=f"todo_{i}"):
            st.session_state.completed.append(task)
            remove_tasks.append(task)
    # Remove completed tasks after loop to avoid modifying list while iterating
    for task in remove_tasks:
        st.session_state.to_do.remove(task)
else:
    st.write("No tasks yet.")

# Display completed tasks
st.subheader("✅ Completed Tasks:")
if st.session_state.completed:
    for task in st.session_state.completed:
        st.markdown(f"- ~~{task}~~")
else:
    st.write("No completed tasks yet.")
