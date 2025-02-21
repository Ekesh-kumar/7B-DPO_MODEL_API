from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
import json
import os
import dotenv

dotenv.load_dotenv()

def generate_screen_analysis(screen_text: str, llm) -> dict:
    prompt = f"""
    You are an advanced AI specializing in screen analysis. Analyze the following screen text and extract structured JSON information,
    from given analysis of screen, you need to give json data, which includes all the options available, all the input fields and their serial numbers, screen name.
    if multiple sections are their for options, put it in seperate key, 
    ### **Screen Text:**
    {screen_text}

    ### * clasify the information and give the data in json format
    """

    response = llm.predict(prompt)  
    response_text = response.content if hasattr(response, 'content') else str(response)

    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON from LLM response"}


screen_analysis_tool = Tool(
    name="Screen Analysis Generator",
    func=lambda x: json.dumps(generate_screen_analysis(x, llm), indent=4),
    description="Generates structured JSON data from screen text analysis."
)


openai_api_key = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
agent = initialize_agent(
    tools=[screen_analysis_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def getJson(analysis) : 
    response = agent.run(analysis)
    return response
