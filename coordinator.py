import os
from agent_config import CLINICAL_TOOLS
from dotenv import load_dotenv
from google import genai
from mcp_server import ClinicalMCPServer

load_dotenv()

class AICoordinator:
    def __init__(self):
        # Initialize client for AI Studio
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        
        # Use the EXACT model name found in your discovery script
        self.model_id = "gemini-2.5-flash"
        
        self.mcp = ClinicalMCPServer()
        
        # Define tools using dictionary format for maximum stability
        self.tools = CLINICAL_TOOLS
        print(f"Coordinator initialized with model: {self.model_id}")

    def run_full_cycle(self, agent_instructions, user_prompt):
        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                config={"system_instruction": agent_instructions, "tools": self.tools},
                contents=user_prompt
            )

            if response.candidates[0].content.parts and response.candidates[0].content.parts[0].function_call:
                call = response.candidates[0].content.parts[0].function_call
                print(f"DEBUG: Agent calling tool {call.name}...")
                
                # Execute tool
                tool_result = self.mcp.call_tool(call.name, call.args)
                
                # Send back to Gemini
                final_response = self.client.models.generate_content(
                    model=self.model_id,
                    config={"system_instruction": agent_instructions, "tools": self.tools},
                    contents=[
                        {"role": "user", "parts": [{"text": user_prompt}]},
                        response.candidates[0].content,
                        {"role": "model", "parts": [{"function_response": {"name": call.name, "response": {"result": tool_result}}}]}
                    ]
                )
                return final_response.text
            return response.text
        except Exception as e:
            return f"System Error: {str(e)}"