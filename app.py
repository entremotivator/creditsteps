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
    {"step": "Reduce Credit Card Balances", "substeps": [
        "Aim to keep credit utilization below 30% of your credit limit.",
        "Pay down high-interest credit cards first (debt avalanche method).",
        "Avoid maxing out your credit cards to maintain a healthy score."
    ], "notes": ""},
    {"step": "Increase Your Credit Limits", "substeps": [
        "Request a credit limit increase from your credit card issuer.",
        "Avoid increasing your spending after getting a higher limit.",
        "Demonstrate responsible usage to maintain a low utilization rate."
    ], "notes": ""},
    {"step": "Avoid Closing Old Credit Accounts", "substeps": [
        "Keep older credit accounts open to maintain account age.",
        "Use inactive accounts occasionally to prevent closure.",
        "Monitor fees or changes in terms on older accounts."
    ], "notes": ""},
    {"step": "Diversify Credit Types", "substeps": [
        "Obtain a mix of credit accounts (e.g., credit card, mortgage, car loan).",
        "Avoid opening too many accounts in a short period.",
        "Show responsible payment history across all accounts."
    ], "notes": ""},
    {"step": "Keep Credit Inquiries Minimal", "substeps": [
        "Avoid frequent applications for credit, which trigger hard inquiries.",
        "Check pre-approval offers to minimize unnecessary inquiries.",
        "Space out applications by 6 months to 1 year when possible."
    ], "notes": ""},
    {"step": "Settle Collection Accounts", "substeps": [
        "Negotiate with collection agencies to settle accounts.",
        "Request a 'pay-for-delete' arrangement if possible.",
        "Ensure paid accounts are updated in your credit report."
    ], "notes": ""},
    {"step": "Use Secured Credit Cards (If Necessary)", "substeps": [
        "Open a secured credit card to rebuild credit if needed.",
        "Make small, manageable purchases and pay in full monthly.",
        "Monitor credit score improvement over 6–12 months."
    ], "notes": ""},
    {"step": "Maintain Low Balances on Revolving Accounts", "substeps": [
        "Pay off balances before the statement closes.",
        "Avoid carrying balances even if no interest is charged.",
        "Monitor credit utilization via online tools."
    ], "notes": ""},
    {"step": "Avoid Late Payments", "substeps": [
        "Create a budget to ensure you have funds to cover bills.",
        "Set up calendar reminders to never miss due dates.",
        "Contact creditors immediately if you anticipate being late."
    ], "notes": ""},
    {"step": "Use Less Than 10% of Your Credit Limit", "substeps": [
        "Keep utilization at or below 10% for optimal scoring.",
        "Pay off balances mid-cycle to free up credit before the billing date.",
        "Track usage through your credit card app or statements."
    ], "notes": ""},
    {"step": "Add Positive Payment History", "substeps": [
        "Consider services like Experian Boost to report utilities and rent.",
        "Ensure all payments on reported accounts are timely.",
        "Verify that positive history is reflected in your reports."
    ], "notes": ""},
    {"step": "Monitor Your Credit Score Regularly", "substeps": [
        "Use free services like Credit Karma or your bank’s credit tools.",
        "Check for sudden changes and investigate discrepancies.",
        "Set alerts for changes in your credit profile."
    ], "notes": ""},
    {"step": "Avoid Payday Loans", "substeps": [
        "Explore alternatives like personal loans or financial counseling.",
        "Pay off existing payday loans to stop compounding fees.",
        "Build an emergency fund to avoid needing quick cash options."
    ], "notes": ""},
    {"step": "Keep Employment Consistent", "substeps": [
        "Maintain steady employment to demonstrate financial stability.",
        "Provide clear proof of income when applying for credit.",
        "Avoid significant employment gaps, if possible."
    ], "notes": ""},
    {"step": "Negotiate Credit Card Interest Rates", "substeps": [
        "Call your card issuer to request a lower interest rate.",
        "Provide reasons like a good payment history or better offers elsewhere.",
        "Ensure rate reductions are confirmed in writing."
    ], "notes": ""},
    {"step": "Pay Off High-Interest Debts First", "substeps": [
        "Use the debt avalanche method to minimize total interest paid.",
        "Focus on one account while making minimum payments on others.",
        "Track progress using a debt repayment calculator."
    ], "notes": ""},
    {"step": "Avoid Co-Signing Loans", "substeps": [
        "Understand that co-signing makes you equally responsible for the debt.",
        "Avoid it unless you’re confident in the borrower’s reliability.",
        "Monitor the account if you’ve already co-signed."
    ], "notes": ""},
    {"step": "Build an Emergency Fund", "substeps": [
        "Save at least 3–6 months of expenses to cover unexpected costs.",
        "Use a high-yield savings account for better returns.",
        "Automate contributions to make saving consistent."
    ], "notes": ""},
    {"step": "Leverage Balance Transfer Offers", "substeps": [
        "Transfer high-interest balances to a 0% APR card if eligible.",
        "Pay off the transferred balance during the promotional period.",
        "Avoid new purchases on the transfer card."
    ], "notes": ""},
    {"step": "Track Spending Habits", "substeps": [
        "Use budgeting apps like Mint or YNAB to track expenses.",
        "Identify areas where you can cut unnecessary spending.",
        "Reallocate savings toward debt repayment or emergency funds."
    ], "notes": ""},
    {"step": "Limit New Credit Applications", "substeps": [
        "Only apply for new credit when necessary.",
        "Research cards or loans before applying to avoid denials.",
        "Space applications to avoid hard inquiry penalties."
    ], "notes": ""},
    {"step": "Take Advantage of Credit Counseling", "substeps": [
        "Find nonprofit credit counseling agencies for expert advice.",
        "Create a personalized action plan for improving your credit.",
        "Follow through with the plan and monitor progress."
    ], "notes": ""},
    {"step": "Stay Patient and Persistent", "substeps": [
        "Understand that building an 850 credit score takes time.",
        "Celebrate small milestones along the way.",
        "Stay consistent with good credit habits over the long term."
    ], "notes": ""}
]

# Load checklist data
if "checklist_data" not in st.session_state:
    st.session_state.checklist_data = real_steps
else:
    real_steps = st.session_state.checklist_data

# Main checklist display
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

# Save back to session state
st.session_state.checklist_data = real_steps

# Progress tracking
completed_steps = sum(
    all(substep["checked"] for substep in step["substeps"]) for step in real_steps
)
total_steps = len(real_steps)
st.markdown(f"### Progress: {completed_steps}/{total_steps} main steps completed!")

# Download functionality
if st.button("Download Checklist Data"):
    data_str = json.dumps(st.session_state.checklist_data, indent=2)
    st.download_button(
        label="Download JSON",
        data=data_str,
        file_name="credit_score_checklist.json",
        mime="application/json"
    )

