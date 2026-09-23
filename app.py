import streamlit as st

from agents.orchestrator import OrchestratorAgent


st.set_page_config(
    page_title="Insurance Claims AI",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Insurance Claims Agentic AI")
st.caption("AI-assisted insurance claims decision-support prototype")

st.divider()

st.subheader("📋 Claim Information")

claim = st.text_area(
    "Enter insurance claim details",
    placeholder="Example: Car accident claim - vehicle damaged in a collision. Repair estimate is 85000 INR.",
    height=150
)

if st.button("🔍 Analyze Claim", type="primary"):

    if not claim.strip():
        st.warning("Please enter claim details.")
    else:
        with st.spinner("Running multi-agent claim analysis..."):

            orchestrator = OrchestratorAgent()
            result = orchestrator.run(claim)

        st.success("Claim analysis completed.")

        st.subheader("📝 Claims Assessment Report")

        st.text(result)

st.divider()

st.info(
    "⚠️ This is an educational decision-support prototype. "
    "It does not automatically approve, reject, or establish fraud. "
    "Final decisions require authorized human review."
)