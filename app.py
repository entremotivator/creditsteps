import streamlit as st
import json

# Title and description
st.title("850 Credit Score Checklist")
st.subheader("Achieve Financial Excellence: Your Comprehensive 30-Step Guide")
st.markdown("""
This app provides **30 actionable steps**, each with **3 specific substeps**, to help you improve and maintain a perfect credit score.  
You can:  
1. Check off completed tasks.  
2. Add personal notes for each step.  
3. Track progress and download your checklist.  
Let's start building your roadmap to financial excellence!
""")

# Real credit improvement steps
real_steps = [
    {"step": "Review Your Credit Report", "substeps": [
        "Obtain a free credit report from AnnualCreditReport.com.",
        "Check for errors, such as incorrect balances or missed payments.",
        "Dispute inaccuracies with the credit bureau promptly."
    ], "notes": ""},
    {"step": "Pay Bills on Time", "substeps": [
        "Set up automatic payments or reminders for due dates.",
        "Prioritize at least the minimum payment to avoid late fees.",
        "Catch up on any past-due accounts to reduce negative impact."
    ], "notes": ""},
    # Add other steps here as needed for your checklist
]

# Initialize session state
if "checklist_data" not in st.session_state:
    st.session_state.checklist_data = real_steps
else:
    real_steps = st.session_state.checklist_data

# Display checklist
for i, step in enumerate(real_steps):
    st.subheader(step["step"])
    
    # Substep checklist
    for j, substep in enumerate(step["substeps"]):
        key = f"step_{i}_substep_{j}"
        checked = st.checkbox(substep, key=key)
        real_steps[i]["substeps"][j] = {"text": substep, "checked": checked}
    
    # Notes section
    note_key = f"step_{i}_notes"
    real_steps[i]["notes"] = st.text_area(
        f"Notes for {step['step']}",
        value=real_steps[i]["notes"],
        key=note_key
    )

# Save updated state
st.session_state.checklist_data = real_steps

# Progress tracking
completed_steps = sum(
    all(substep["checked"] for substep in step["substeps"]) for step in real_steps
)
total_steps = len(real_steps)
st.markdown(f"### Progress: {completed_steps}/{total_steps} main steps completed!")

# Download checklist data
if st.button("Download Checklist Data"):
    data_str = json.dumps(st.session_state.checklist_data, indent=2)
    st.download_button(
        label="Download JSON",
        data=data_str,
        file_name="credit_score_checklist.json",
        mime="application/json"
    )
