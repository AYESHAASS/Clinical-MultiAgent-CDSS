import json
import re
import time
from coordinator import AICoordinator
from agents.validator_agent import ClinicalValidator
from agents.predictor_agent import PredictorAgent
from agents.guideline_agent import GuidelineAgent
from agents.auditor_agent import AuditorAgent

class ClinicalOrchestrator:
    def __init__(self):
        self.coordinator = AICoordinator()
        self.validator = ClinicalValidator()
        self.predictor = PredictorAgent()
        self.guideline = GuidelineAgent()
        self.auditor = AuditorAgent()

    def clean_json(self, text):
        # Strip away backticks and "json" labels
        clean = re.sub(r'```json|```', '', text).strip()
        return clean

    def run(self, user_input):
        print("\n[PHASE 1] Validating and Extracting...")
        raw_data = self.coordinator.run_full_cycle(self.validator.get_system_instructions(), user_input)
        
        # CRITICAL SAFETY BYPASS: If Validator flags an emergency, skip the rest.
        if "EMERGENCY_ALERT" in raw_data:
            print("!!! EMERGENCY DETECTED: Bypassing Model Pipeline !!!")
            return raw_data

        json_data = self.clean_json(raw_data)
        time.sleep(15) 
        
        print("[PHASE 2] Running ML Prediction...")
        prediction_output = self.coordinator.run_full_cycle(self.predictor.get_system_instructions(), f"Predict for: {json_data}")
        time.sleep(5) 
        
        print("[PHASE 3] Searching Clinical Guidelines...")
        guideline_output = self.coordinator.run_full_cycle(self.guideline.get_system_instructions(), f"Guidelines for: {json_data}")
        time.sleep(5) 
        
        print("[PHASE 4] Final Clinical Audit...")
        final_context = f"PATIENT DATA: {json_data}\n\nMODEL OUTPUT: {prediction_output}\n\nGUIDELINES: {guideline_output}"
        final_report = self.coordinator.run_full_cycle(self.auditor.get_system_instructions(), final_context)
        
        return final_report

if __name__ == "__main__":
    orchestrator = ClinicalOrchestrator()
    # Test Scenario
    patient_story = "I am 50 years old, glucose 210, 2 pregnancies, BP 120, Skin 30, Insulin 120, BMI 32, Pedigree 0.5"
    report = orchestrator.run(patient_story)
    print("\n--- FINAL CLINICAL REPORT ---")
    print(report)