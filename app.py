import streamlit as st

from agents.orchestrator import OrchestratorAgent


st.set_page_config(
    page_title="Insurance Claims AI",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Insurance Claims Agentic AI")
st.caption("AI-assisted insurance claims decision-support platform")

st.divider()

st.subheader("📋 Claim Information")

claim = st.text_area(
    "Enter insurance claim details",
    placeholder=(
        "Example: Car accident claim - vehicle damaged in a collision. "
        "Repair estimate is 85000 INR."
    ),
    height=150
)


if st.button(
    "🔍 Analyze Claim",
    type="primary",
    use_container_width=True
):

    if not claim.strip():

        st.warning("Please enter claim details before analysis.")

    else:

        with st.spinner("Running multi-agent claim analysis..."):

            orchestrator = OrchestratorAgent()
            result = orchestrator.run(claim)

        st.success("✅ Claim analysis completed successfully.")

        st.divider()

        st.subheader("📊 Analysis Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("📄 Documents", "Reviewed")

        with col2:
            st.metric("📋 Policy", "Retrieved")

        with col3:
            st.metric("🔎 Assessment", "Completed")

        with col4:
            st.metric("🚨 Fraud", "Indicators Checked")

        st.divider()

        # Cleanly extract each section from the report

        document_section = result.split(
            "📄 Document Review\n------------------\n", 1
        )[1].split(
            "📋 Policy Review", 1
        )[0].strip()

        policy_section = result.split(
            "📋 Policy Review\n----------------\n", 1
        )[1].split(
            "🔎 Claim Assessment", 1
        )[0].strip()

        assessment_section = result.split(
            "🔎 Claim Assessment\n-------------------\n", 1
        )[1].split(
            "🚨 Fraud Indicator Review", 1
        )[0].strip()

        fraud_section = result.split(
            "🚨 Fraud Indicator Review\n-------------------------\n", 1
        )[1].split(
            "👨‍💼 Human Review", 1
        )[0].strip()

        human_section = result.split(
            "👨‍💼 Human Review\n----------------\n", 1
        )[1].strip()


        st.subheader("📄 Document Review")

        with st.expander(
            "View Document Findings",
            expanded=True
        ):
            st.write(document_section)


        st.subheader("📋 Policy Review")

        with st.expander(
            "View Retrieved Policy Information",
            expanded=True
        ):
            st.write(policy_section)


        st.subheader("🔎 Claim Assessment")

        with st.expander(
            "View Assessment Details",
            expanded=True
        ):
            st.write(assessment_section)


        st.subheader("🚨 Fraud Indicator Review")

        with st.expander(
            "View Fraud Indicators",
            expanded=True
        ):
            st.write(fraud_section)


        st.subheader("👨‍💼 Human Review")

        st.info(
            "Final claim decisions require review by an "
            "authorized insurance professional."
        )

        with st.expander("View Human Review Details"):
            st.write(human_section)


st.divider()

st.warning(
    "⚠️ Educational decision-support prototype. "
    "This system does not automatically approve or reject claims "
    "and does not establish fraud. Final decisions require "
    "authorized human review."
)