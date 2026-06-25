# Tool definitions for the Clinical Multi-Agent System

PREDICTOR_TOOL = {
    "name": "predict_diabetes",
    "description": "Calculates diabetes risk using 8 clinical features (Age, BMI, Glucose, etc.).",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "pregnancies": {"type": "NUMBER"},
            "glucose": {"type": "NUMBER"},
            "bp": {"type": "NUMBER"},
            "skin": {"type": "NUMBER"},
            "insulin": {"type": "NUMBER"},
            "bmi": {"type": "NUMBER"},
            "dpf": {"type": "NUMBER"},
            "age": {"type": "NUMBER"}
        },
        "required": ["pregnancies", "glucose", "bp", "skin", "insulin", "bmi", "dpf", "age"]
    }
}

RAG_TOOL = {
    "name": "search_guidelines",
    "description": "Retrieves medical diagnostic thresholds from the clinical knowledge base.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "query": {"type": "STRING"}
        },
        "required": ["query"]
    }
}

CLINICAL_TOOLS = [{"function_declarations": [PREDICTOR_TOOL, RAG_TOOL]}]