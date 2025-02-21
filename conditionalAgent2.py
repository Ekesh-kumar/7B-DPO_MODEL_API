import os
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import logging

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key, temperature=0.3)
logging.basicConfig(level=logging.DEBUG)

@tool
def analyze_screen(screen_data: str, task_prompt :str) -> str:

    prompt = f"""
    Given the following screen data:
    {screen_data}
    
    And the following task prompt:
    {task_prompt}
    
    Determine if the task can be executed based on the screen's current state. If possible, 
    list the steps to execute it. If not, return "Operation is not possible."
    """
    
     
tools = [analyze_screen]

agent = create_react_agent(model=model, tools=tools)

input_message = HumanMessage(content="screen data is : A login page with username and password fields and task_prompt is :Login with user 'admin' and password '1234',   analyse screen.")

result = agent.invoke({"messages": [input_message]})

# Output the result
print(result["messages"][-1].content)
