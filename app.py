# pyright: reportMissingImports=false


import streamlit as st
from crew_setup import run_microplan

st.set_page_config(page_title="MicroPlan AI", layout="centered")

st.title("MicroPlan AI")

user_input = st.text_input(
    "Describe your situation in one sentence:",
    placeholder="e.g. I have 30 minutes and feel mentally tired"
)

if st.button("Generate Micro-Plan") and user_input:
    with st.spinner("Thinking..."):
        result = run_microplan(user_input)

    st.markdown("Your Personalized Micro-Plan")
    st.write(result["plan"])
