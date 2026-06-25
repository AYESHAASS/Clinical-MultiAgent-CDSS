from tools.prediction_utility import get_diabetes_prediction
from tools.search_utility import search_clinical_guidelines

class ClinicalMCPServer:
    def __init__(self):
        self.tools = {
            "predict_diabetes": get_diabetes_prediction,
            "search_guidelines": search_clinical_guidelines
        }

    def call_tool(self, tool_name, params):
        if tool_name not in self.tools:
            return {"error": f"Tool {tool_name} not found."}
        
        print(f"MCP Server: Executing {tool_name}...")
        # This unpacking allows the tool to receive its arguments
        return self.tools[tool_name](**params)

# This allows us to test the server bridge independently
if __name__ == "__main__":
    server = ClinicalMCPServer()
    # Testing the search tool through the MCP bridge
    test_search = server.call_tool("search_guidelines", {"query": "diagnostic"})
    print("MCP Search Test:", "Success" if "Table" in test_search else "Failed")