class PredictorAgent:
    def __init__(self):
        self.name = "Risk Analyst"

    def get_system_instructions(self):
        return """
        You are a Medical Data Analyst. 
        Your only job is to take clinical data and use the 'predict_diabetes' tool.
        Report the risk category and the confidence score. 
        Do not give medical advice.
        """