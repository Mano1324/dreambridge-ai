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

import streamlit as st
import docx2txt
import PyPDF2
import os
import openai

st.set_page_config(page_title="DreamBridge AI")

st.title("DreamBridge AI ✨")

option = st.selectbox(
    "Choose a feature:",
    ["SOP Reviewer", "Scholarship Finder", "Application Checklist"]
)

if option == "SOP Reviewer":
    st.header("📄 SOP Reviewer")
    
    uploaded_file = st.file_uploader("Upload your SOP file", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        file_text = ""

        # Extract text from uploaded file
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                file_text += page.extract_text()
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            file_text = docx2txt.process(uploaded_file)
        elif uploaded_file.type == "text/plain":
            file_text = uploaded_file.read().decode("utf-8")
        
        st.success("File uploaded and content extracted!")
        st.text_area("Extracted SOP Text", file_text, height=300)

        if st.button("Review My SOP"):
            with st.spinner("Analyzing your SOP using AI..."):
                openai.api_key = os.getenv("OPENAI_API_KEY")

                prompt = f"You're an expert university reviewer. Please evaluate this SOP and give suggestions for clarity, grammar, structure, and impact:\n\n{file_text}"

                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=600
                )

                feedback = response["choices"][0]["message"]["content"]
                st.markdown("### 📝 AI Review Feedback:")
                st.write(feedback)

    st.write("Upload your Statement of Purpose and I'll review it for clarity, grammar, and structure.")
elif option == "Scholarship Finder":
    st.write("Tell me your background and I'll list matching scholarships.")
elif option == "Application Checklist":
    st.write("I'll guide you through everything needed to apply for international universities.")
