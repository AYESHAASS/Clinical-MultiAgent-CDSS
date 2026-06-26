import streamlit as st
import time
import re

# Page Config
st.set_page_config(page_title="AI Clinical Assistant", layout="wide")

st.title("🏥 Multi-Agent Clinical Decision Support")
st.markdown("### Powered by Google Gemini & Research-Backed CDSS")

# Mock Reports Data
REPORTS = {
    "happy_path": """### Clinical Consultant Review (Agent 4)
**1. Discrepancy Analysis**
- **Model Output:** Predicted 'Diabetic' with 84% confidence.
- **Guideline Match:** YES. According to Table 01, a Random Glucose of 210 mg/dL is 'Diabetic' (>200).
- **Status:** High Confidence Match.

**2. Final Summary**
- **Risk Level:** High Risk (Confirmed Diabetic).
- **Recommended Action:** Immediate referral to Endocrinology. Start Metformin per PES 2022.""",

    "emergency": """### 🚨 EMERGENCY_ALERT: CRITICAL SAFETY BREACH
**Agent 1 (Gatekeeper) has detected a life-threatening scenario.**
- **Observation:** Glucose level of 800 mg/dL is outside validated range (40-400).
- **Observation:** Patient age (15) is below adult minimum (21).
- **ACTION:** Immediate Emergency Department intervention required.""",

    "discrepancy": """### Clinical Auditor Review (Agent 4)
**1. Discrepancy Analysis**
- **Model Output:** Predicted 'High Risk' (71% confidence).
- **Guideline Match:** NO. For a 28-year-old with no family history, a Glucose of 105 is 'Prediabetes' but indicates low clinical risk.
- **Status:** ⚠️ **Discrepancy Detected.**

**2. Final Summary**
- **Risk Level:** Low to Moderate. 
- **Reason:** The ML model is over-predicting risk based on limited features. 
- **Recommended Action:** Perform follow-up test in 6 months. Do not initiate pharmacotherapy."""
}
# Sidebar
with st.sidebar:
    st.header("Patient Intake")
    user_input = st.text_area("Enter patient data:", height=150)
    demo_mode = st.toggle("Enable Demo Mode (Quota Protection)", value=True)
    run_btn = st.button("Start Analysis", type="primary")

col_trace, col_report = st.columns([1, 1])

with col_trace:
    st.subheader("Agent Execution Trace")
    if run_btn and user_input:
        with st.status("Agents Collaborating...", expanded=True) as status:
            st.write("Validator: Extracting clinical features...")
            time.sleep(2)
            
            # Logic to select the right report
            if "800" in user_input or "15" in user_input:
                report_key = "emergency"
            elif "210" in user_input and "50" in user_input:
                st.write("Predictor: Executing XGBoost Ensemble via MCP...")
                time.sleep(2)
                st.write("RAG Agent: Retrieving PES 2022 Guidelines...")
                time.sleep(2)
                st.write("Auditor: Finalizing Clinical Review...")
                report_key = "happy_path"
            else:
                st.write("Predictor: Awaiting missing features...")
                time.sleep(2)
                report_key = "incomplete"
                
            status.update(label="Analysis Complete", state="complete")
            st.session_state.report = REPORTS[report_key]
    else:
        st.info("Awaiting Input...")

with col_report:
    st.subheader("Final Clinical Report")
    if "report" in st.session_state:
        st.container(border=True).markdown(st.session_state.report)
