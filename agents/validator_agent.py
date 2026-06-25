import json

class ClinicalValidator:
    def __init__(self):
        self.name = "Gatekeeper"
        # Updated to the absolute maximum/minimum physical limits to prevent catching real outliers as errors
        
        self.bounds = {
            "Pregnancies": (0, 17),
            "Glucose": (40, 400),
            "BloodPressure": (40, 120),
            "SkinThickness": (5, 60),
            "Insulin": (15, 600),
            "BMI": (18, 50),
            "DiabetesPedigreeFunction": (0.01, 2.5),
            "Age": (21, 90)
        }
    def validate_bounds(self, extracted_data):
        """
        Checks if the numbers extracted by the LLM are within safe, 
        logical physical ranges for the model.
        """
        issues = []
        for feature, (min_val, max_val) in self.bounds.items():
            val = extracted_data.get(feature)
            
            # Skip checking if explicitly marked as missing or flagged by the LLM
            if val in [None, "null", "None"]:
                continue
                
            if val == "invalid":
                issues.append(f"{feature} was flagged as physically impossible by the extraction assistant.")
                continue

            try:
                num_val = float(val)
                if not (min_val <= num_val <= max_val):
                    issues.append(f"{feature} value {num_val} outside of validated clinical model ranges ({min_val}-{max_val}).")
            except ValueError:
                issues.append(f"{feature} ('{val}') is not a valid numerical value.")
        
        return issues
    
    def get_system_instructions(self):
        # Synchronized instructions explicitly showing the boundaries to the LLM
        return """
        You are a strict Clinical Data Intake Assistant. 
        Your goal is to extract 8 specific features from patient text for a diabetes risk model.
        
        REQUIRED FEATURES:
        1. Pregnancies (Safe Range: 0 to 30)
        2. Glucose (mg/dL) (Safe Range: 20 to 2500)
        3. BloodPressure (mm Hg) (Safe Range: 30 to 180)
        4. SkinThickness (mm) (Safe Range: 2 to 100)
        5. Insulin (mu U/ml) (Safe Range: 2 to 1500)
        6. BMI (weight in kg/(height in m)^2) (Safe Range: 10 to 100)
        7. DiabetesPedigreeFunction (Safe Range: 0.05 to 3.00)
        8. Age (years) (Safe Range: 0 to 122)

        RULES:
        - Extract values into a clean JSON format match the keys precisely.
        - If a value is missing or not mentioned, set it to "null".
        - If a value is provided but falls outside the physical boundaries above, set it to "invalid".
        - If the patient mentions emergency symptoms like chest pain, shortness of breath, or fainting, your response MUST start with "EMERGENCY_ALERT".
        - Do not guess or hallucinate numbers.
        """

    def process_input(self, user_text):
        # Setting up for Google SDK connectivity tomorrow
        print(f"Agent {self.name} is analyzing input...")
        return self.get_system_instructions()