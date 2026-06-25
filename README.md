# 🏥 Clinical Multi-Agent Decision Support System (CDSS)

### Developed for the Google AI Agents Capstone Project

## 🔬 Research Foundation
This project is a production-ready implementation of clinical research focused on diabetes management. As a first-author researcher published in **Springer Nature**, I developed this system to bridge the gap between static machine learning models and active clinical reasoning. 

* **Original Paper:** [https://doi.org/10.1007/s13410-026-01658-3]
* **Core Methodology:** Bridging XGBoost predictive ensembles with grounded medical guidelines (ADA 2023 / PES 2022).

## 🏗️ System Architecture
The system uses a four-agent pipeline orchestrated via the **Google Agent Development Kit (ADK)** and an **MCP Server** bridge.

![System Architecture](CAPSTONE%20IMG.png)

### The Agents:
1.  **Clinical Validator (The Gatekeeper):** Handles data extraction, PII masking, and physiological bounds checking.
2.  **Risk Predictor:** Executes a custom XGBoost ensemble via a standardized MCP tool.
3.  **Guideline RAG:** Retrieves medical diagnostic thresholds from a specialized Markdown knowledge base.
4.  **Clinical Auditor (Chief Resident):** Cross-references model output with medical truth to identify discrepancies.

## 🛡️ Safety and Security
* **Emergency Bypass:** Immediate hospital referral triggers if glucose > 400 mg/dL or age < 21.
* **Privacy:** Automatic PII filtering at the validation stage.
* **Logic Integrity:** The Auditor flags model "hallucinations" if they contradict established medical guidelines.

## 🚀 How to Run
1. Clone this repository.
2. Create a `.env` file with your `GOOGLE_API_KEY` and `HF_TOKEN`.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the UI: `streamlit run app.py`

## 📺 Demo Video
Watch the full architectural walkthrough and live clinical simulation run on YouTube:

[![Clinical CDSS Architecture Demo](https://img.youtube.com/vi/qZEX1wmUGzU/0.jpg)](https://youtu.be/qZEX1wmUGzU)

*Click the image above to view the demonstration video.*