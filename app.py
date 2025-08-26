"""
TalentScout - Multi-step Flow (Intro → Form → Confirmation → Chatbot)
"""

import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

st.set_page_config(page_title="TalentScout - Hiring Assistant", layout="centered")

st.title("🤖 TalentScout — Hiring Assistant")

# ---- Session State ----
if "step" not in st.session_state:
    st.session_state.step = "intro"   # intro → form → confirm → chat
if "candidate_details" not in st.session_state:
    st.session_state.candidate_details = {}
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": 
         "You are TalentScout, a professional but friendly AI hiring assistant. "
         "Follow these steps: "
         "1) Introduce yourself and ask permission. "
         "2) If user agrees, collect details through a form. "
         "3) Confirm details. "
         "4) Conduct an interview with short, tailored, relevant questions "
         "based on candidate experience and tech stack. "
         "Do not repeat the same question unless the candidate gives an invalid or unclear answer. "
         "Keep the conversation engaging but professional."}
    ]


# ---- Step 1: Intro ----
if st.session_state.step == "intro":
    st.chat_message("assistant").markdown(
        "Hello! I’m **TalentScout**, your AI hiring assistant. "
        "Would you like to continue with the process?"
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Yes, Continue"):
            st.session_state.step = "form"
            st.rerun()
    with col2:
        if st.button("❌ Exit"):
            st.stop()


# ---- Step 2: Candidate Form ----
elif st.session_state.step == "form":
    st.write("Please fill in your details below:")
    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        experience = st.number_input("Years of Experience", min_value=0, step=1)
        tech_stack = st.text_area("Your Tech Stack (comma separated, e.g., Python, SQL, Flask)")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.candidate_details = {
                "name": name,
                "email": email,
                "experience": experience,
                "tech_stack": tech_stack
            }
            st.session_state.step = "confirm"
            st.rerun()


# ---- Step 3: Confirm Details ----
elif st.session_state.step == "confirm":
    details = st.session_state.candidate_details
    st.chat_message("assistant").markdown(
        f"Thanks **{details['name']}**! Here are the details you submitted:\n\n"
        f"- **Email:** {details['email']}\n"
        f"- **Experience:** {details['experience']} years\n"
        f"- **Tech Stack:** {details['tech_stack']}\n\n"
        "Are you ready to start answering interview questions?"
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Yes, Start Questions"):
            st.session_state.step = "chat"
            st.rerun()
    with col2:
        if st.button("🔙 Go Back"):
            st.session_state.step = "form"
            st.rerun()


# ---- Step 4: Chatbot Interview ----
elif st.session_state.step == "chat":
    # Function to call Groq LLM
    def call_llm(messages):
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
            temperature=0.7,
            max_tokens=512
        )
        return response.choices[0].message.content

    details = st.session_state.candidate_details
    tech_stack = details['tech_stack']

    # If chat just started, ask the first tailored interview question
    if len(st.session_state.messages) == 1:  # only system prompt exists
        context = {
            "role": "system",
            "content": (
                f"Candidate Details: Name={details['name']}, Email={details['email']}, "
                f"Experience={details['experience']} years, Tech Stack={tech_stack}. "
                f"You are TalentScout, a professional interviewer. "
                f"Start with an introductory question about their experience, then ask "
                f"short, specific, and varied technical questions directly based on their tech stack. "
                f"Rotate between different technologies instead of sticking to one topic. "
                f"Occasionally include scenario-based or problem-solving questions. "
                f"Keep questions concise and clear, one at a time."
            )
        }
        st.session_state.messages.append(context)

        first_q = call_llm(st.session_state.messages + [
            {"role": "user", "content": "Start the interview with the first tailored question."}
        ])
        st.session_state.messages.append({"role": "assistant", "content": first_q})

    # Show chat history
    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            with st.chat_message("assistant"):
                st.markdown(msg["content"])
        elif msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])

    # User input
    user_input = st.chat_input("Type your response here...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        next_q = call_llm(st.session_state.messages + [
            {"role": "system", "content": (
                "Now ask the next interview question. "
                "Always vary the topic within the candidate’s tech stack. "
                "Mix theory, practical application, and problem-solving. "
                "Avoid repeating previous questions."
            )}
        ])
        st.session_state.messages.append({"role": "assistant", "content": next_q})

        st.rerun()
