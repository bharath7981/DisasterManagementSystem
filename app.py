import streamlit as st
import google.generativeai as genai

SYSTEM_PROMPT = """
You are a Disaster Management Response & Relief Process Explainer Bot.

Your only purpose is to explain disaster response and relief processes
in a simple, polite, and calm manner for public awareness.

STRICT RULES:
1. You are INFORMATION-ONLY.
2. Respond ONLY to:
   - Evacuation procedures
   - Relief camp processes
   - Disaster response stages
   - Basic safety precautions
3. Do NOT give predictions, alerts, rescue steps, or emergency commands.
4. Do NOT add extra information.
5. Use simple words and short sentences.
6. Be polite and calm.
7. Avoid panic or urgency.

If a question is outside scope, reply:
"I am designed only to explain general disaster response and relief processes for awareness."
"""


import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT,
    generation_config={
        "temperature":0.25
    }
)

st.set_page_config(
    page_title="Disaster Response Explainer Bot",
    page_icon="",
    layout="centered"
)

st.title("Disaster Management Response & Relief Bot")
st.write(
    "This bot explains disaster response and relief processes "
    "in a simple and calm manner for public awareness."
)

user_input = st.text_area(
    "Ask your question:",
    placeholder="Example: Explain evacuation procedures"
)

if st.button("Get Explanation"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):
            response = model.generate_content(user_input)
            st.success("Explanation")
            st.write(response.text)

st.markdown("---")
st.caption(
    "ℹThis bot provides general information only. "
    "It does not issue alerts or emergency instructions."
)
