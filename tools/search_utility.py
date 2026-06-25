import os

def search_clinical_guidelines(query=None):
    # We ignore the query and just return the ground truth
    file_path = os.path.join("knowledge_base", "guidelines.md")
    try:
        if not os.path.exists(file_path):
            return "Error: Medical guidelines file is missing from the knowledge_base folder."
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We return the first 2000 characters. 
        # This is enough for the tables and targets without crashing the AI.
        return content[:2000]

    except Exception as e:
        return f"Technical Error reading guidelines: {str(e)}"