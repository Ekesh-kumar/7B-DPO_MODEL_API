from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
import dotenv
import os
import json
from summary_agent import Summary_json_agent
from comprehend_agent import ComprehendAgent
from navigation_screen_set import navigation_set
import sys

dotenv.load_dotenv()

class processAgent:

    def perform_process(self, navigation) -> str:
        agent = ComprehendAgent()
        navigation_data = navigation_set()
        navigation_info = navigation_data.get_navigation(navigation)       
        process = navigation_info.get("steps")
        screens = navigation_info.get("screens")
        condition = navigation_info.get("conditions")
        size = len(process)
        summary_agent = Summary_json_agent()
        screen_summary = " "

        for i in range(0, len(screens)) :
            screen_summary = screen_summary + " \n" + summary_agent.get_screen(screens[i])

        print(agent.analyze_process_step(condition[0], process[0], screen_summary))

        return "process completed....."

if __name__ =="__main__":
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    proccess_agent = processAgent()
    navigation = input("Enter the navigation process:")

    if navigation in ["exit", "end"]:
        sys.exit()

    print(proccess_agent.perform_process(navigation))
  