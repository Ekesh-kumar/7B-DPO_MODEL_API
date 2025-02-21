import os
from pydantic import BaseModel
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class process_decider_Agent :

    def __init__(self ):
        openai_api_key = os.environ.get("OPENAI_API_KEY")
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 0.3,openai_api_key=openai_api_key)


    def analyze_screen(self , screen_data, task_prompt) -> str:
        
        prompt = f"""
                Given the following screen data which is in json format :
                {screen_data}
                And the following task prompt:
                {task_prompt}
                ** Determine if the task can be executed based on the screen's current state.
                ** If multiple screens and multiple tasks are provided in then take the screen information mentioned in the task prompt to compare it with perticular screen data.
                ** dont compare a task with unrelated screens. .
                ### **Validation Criteria:**
                - Identify the fields required to execute the task from the given task prompt.
                - Use **semantic matching** to recognize variations in wording (e.g., "Type Y and Enter" ≈ "Press Y and hit Enter" ≈ "Input Y and confirm").
                - Assume that an **input field is always present** unless the screen explicitly states otherwise.
                - If the task requires **pressing a key (e.g., 'Enter')**, assume the system supports this action unless explicitly restricted.
                - If **all** required fields are present in the screen data (or functionally equivalent), return `true`.
                - If **any** required field is **explicitly missing**, return `false`.
                ### **Important Notes:**
                - If an action like "Type or Enter" is required, assume that an **input box exists** and can accept the key press.
                - **Do not be overly strict** with wording—if functionally equivalent elements exist, they should be considered a match.
                - **Strictly return only `true` if tasks mentioned in the prompt are matching the screen data else return `false` dont return any explanations.
                """

        response = self.llm.predict(prompt)

        return response
 
    

