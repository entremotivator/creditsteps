import streamlit as st
import json

# Set up the title and description
st.title("850 Credit Score Checklist")
st.subheader("Track your progress towards achieving an excellent credit score!")
st.markdown("""
This checklist provides 30 steps, each with 3 substeps, to help you achieve an 850 credit score.
You can check off steps, add notes, and track your progress. Your data will be saved locally in your browser.
""")

# Define the checklist
steps = [
    {"step": f"Step {i + 1}", "substeps": [f"Substep {j + 1}" for j in range(3)], "notes": ""}
    for i in range(30)
]

# Load saved data
if "checklist_data" not in st.session_state:
    st.session_state.checklist_data = steps
else:
    steps = st.session_state.checklist_data

# Main app function
for i, step in enumerate(steps):
    st.subheader(step["step"])
    
    # Substep checklist
    for j, substep in enumerate(step["substeps"]):
        key = f"step_{i}_substep_{j}"
        checked = st.checkbox(substep, key=key)
        steps[i]["substeps"][j] = {"text": substep, "checked": checked}
    
    # Notes section
    note_key = f"step_{i}_notes"
    steps[i]["notes"] = st.text_area(f"Notes for {step['step']}", value=steps[i]["notes"], key=note_key)

# Save the data back to session_state
st.session_state.checklist_data = steps

# Display progress
completed = sum(
    all(substep["checked"] for substep in step["substeps"]) for step in steps
)
total_steps = len(steps)
st.markdown(f"### Progress: {completed}/{total_steps} steps completed!")

# Download data
if st.button("Download Checklist Data"):
    data_str = json.dumps(st.session_state.checklist_data, indent=2)
    st.download_button("Download JSON", data_str, "checklist_data.json", "application/json")
