import streamlit as st

st.set_page_config(page_title="DreamBridge AI", page_icon="🌉")

st.title("🌉 DreamBridge AI")
st.write("""
Welcome to **DreamBridge**, your personal AI guide for studying and settling abroad!
""")

st.header("🎯 What can I help you with?")
option = st.selectbox(
    "Choose a feature:",
    ["Select an option", "SOP Reviewer", "Scholarship Finder", "Application Checklist"]
)

if option == "SOP Reviewer":
    st.write("Upload your Statement of Purpose and I'll review it for clarity, grammar, and structure.")
elif option == "Scholarship Finder":
    st.write("Tell me your background and I'll list matching scholarships.")
elif option == "Application Checklist":
    st.write("I'll guide you through everything needed to apply for international universities.")
