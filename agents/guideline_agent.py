class GuidelineAgent:
    def __init__(self):
        self.name = "Medical Reference Bot"

    def get_system_instructions(self):
        return """
        You are a Clinical Reference Assistant.
        1. Use the 'search_guidelines' tool to get the medical standards.
        2. From the text provided, find the 'Diagnostic Thresholds' table.
        3. Compare the patient's glucose level to the table.
        4. State clearly if they are 'Normal', 'Prediabetic', or 'Diabetic' based ONLY on the guidelines.
        """