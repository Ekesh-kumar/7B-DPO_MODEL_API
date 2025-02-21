from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
import dotenv
import os
import json

dotenv.load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)


def determine_action_with_gpt(inputs: dict) -> str:
    
    print(inputs)
    screen_data, prompt = inputs.split("|", 1)

 
    full_prompt = (
        f"You are an intelligent agent analyzing a system screen.\n"
        f"Given the analysis of screen {screen_analysis} and  user requirement: {prompt} \n\n"
        "Respond **ONLY** in JSON format with a single key 'action_required'.\n"
        "Do not provide explanations, thoughts, or reasoning. Just output valid JSON.\n"
        "Example response:\n"
        "{\n  action_required : Select option 2 for HEALTHpac 4.0 Test\n}"
    )
    
    response = llm.invoke(full_prompt).content
    try:
        action_response = json.loads(response)
        return json.dumps(action_response, indent=4)
    except json.JSONDecodeError:
        return json.dumps({"error": "Failed to parse JSON from LLM response"}, indent=4)

# Define LangChain tool
action_planner_tool = Tool(
    name="Action Planner",
    func=determine_action_with_gpt,
    description="Analyzes screen text and determines the required action based on user input."
)

agent = initialize_agent(
    tools=[action_planner_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Input values
screen_analysis = """
System Information:
Operating System: CentOS 6.10 (Final) (x86_64)
User: lfrancel
Password Expiry: Never

Menu Title:
System Name: HEALTH COST SOLUTIONS

Menu Options:
HEALTHpac 4.0 Production → Likely the main application for production use.
HEALTHpac 4.0 Test → A testing environment for the application.
Change Password (88) → Allows the user to update their password.
Logout (99) → Ends the session and logs the user out.
User Interaction:
The system prompts: Enter selection please >|what is the action required to select option Logout
"""

input_dict = {"input":{'screen_data' : screen_analysis}}


response = agent.run(input_dict)
print(response)
