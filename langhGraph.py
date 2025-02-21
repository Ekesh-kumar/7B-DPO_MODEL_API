import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
import logging

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key, temperature=0.3)
logging.basicConfig(level=logging.DEBUG)

@tool
def get_weather(city: str) -> str:
    """
    Retrieve the current weather for a specified city.

    Args:
        city (str): The name of the city to get the weather for.

    Returns:
        str: A brief description of the current weather in the specified city.
    """

    if city.lower() in ["nyc", "new york city", "new york"]:
        return "It might be 35 degree in NYC."
    elif city.lower() in ["sf", "san francisco"]:
        return "It's 25 degree in SF."
    else:
        return f"Weather information for {city} is not available."

@tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b

tools = [get_weather, multiply]


agent = create_react_agent(model=model, tools=tools)

input_message = HumanMessage(content="What's the weather in SF city? Multiply the temperature by 2.")

# Run the agent
result = agent.invoke({"messages": [input_message]})

# Output the result
print(result["messages"][-1].content)