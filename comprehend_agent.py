from langchain.chat_models import ChatOpenAI
from navigate_agent import navigation_agent
from langchain.agents import initialize_agent, AgentType
import dotenv
import os
import json
import time
from process_decider_Agent import process_decider_Agent

dotenv.load_dotenv()

class ComprehendAgent:
    
    """
    Comprehend Agent analyzes screen data and checks if a given process step
    can be performed based on the screen elements available.
    """
    def __init__(self ):
        openai_api_key = os.environ.get("OPENAI_API_KEY")
        self.llm = ChatOpenAI(model_name="gpt-4-turbo", temperature = 0.3, openai_api_key=openai_api_key)

    def analyze_process_step(self, process_conditions,  prompt: str, summary:str) -> str:
        """Identifies the action to perform by comprehending JSON data to check for prompt requirement."""
        navigator = navigation_agent()
        process_decider = process_decider_Agent()
        check = process_decider.analyze_screen(summary, prompt)
        print(check)
        process_analysis_results = self.per_screen_process_analyzer(process_conditions, summary)
        print(process_analysis_results)
        if check in ["False", "false"]:
            response = {"action_required": "action not possible"}
        else :
           response = self.llm.predict(
                                f'''  
                                You are an intelligent mainframe terminal agent. Your task is to return ONLY the ordered set of keys required to perform the specified action, given as a prompt.

                                ### **Step 1: Validate Process Conditions**
                                - Analysze the json file - `{process_analysis_results}` and if json file contains any failed conditions, return:
                               
                                ["Condtions failed"] and Do not proceed further.

                                - If all conditions are satisfied, proceed to Step 2.

                                ### **Step 2: Task Execution (Generate Actions)**
                                - Given the screen summary -{summary} in the json format, which contains details of the screen ordered in different key value pairs, which you need to work on.
                                - Given the task for actions to be performed in the text-{prompt}.
                                Instructions for action generation:

                                Clearly determine and list the keys or inputs required, in the correct execution order.
                                Prompt Example:
                                "Login with username 'abc' and password 'bcd'"
                                Ordered Keys Example:
                                ['abc', 'Enter', 'bcd', 'Enter'].
                                 
                                ** If task is to select the option then give what value we need type to select the value.
                                ** If action is to extract any fields from the screen, go through the entire screen info and select the values which best soots for the description.
                                Action Types: 
                                Navigation: Specify keys needed for navigation.
                                Credential Entry: List username/password entries each followed by 'Enter'.
                                Field Extraction: Provide keys required for extracting/interacting with fields.
                                Important:
                                Return only the ordered keys in Python list format.
                                Do NOT include explanations or additional context.
                                """
                                '''
                            )

        return response

    def per_screen_process_analyzer(self,formatted_conditions, screen_data):
                
            prompt = f'''
                        You are an AI assistant responsible for verifying process conditions based on the provided screen data.
                        Your task is to analyze the given conditions and provide an output in the required format.
 
                        ### **Screen Data:**
                        The screen data is structured as JSON, containing fields, subfields, nested arrays, and options.
                        - **Screen Data:** {screen_data}

                        ### **Conditions to Check:**
                        The conditions define the criteria that must be met before proceeding with the process.
                        - **Formatted Conditions JSON:** {formatted_conditions}
                        - if no conditons are specified , then return "All the conditions are satisfied".
                        - **Important:** Field names in conditions **may not exactly match** the screen data keys, so use **semantic understanding** to relate them correctly.

                        ### **Instructions:**
                        1. **Identify and Extract Fields Dynamically:**
                        - Do not assume a single occurrence of a field.
                        - If a field exists inside an **array** (e.g., `benefits[]`), iterate over **all** occurrences.
                        - **Ensure all required fields** related to the condition are checked.

                        2. **Verify Field Values Are Valid:**
                        - A field is **invalid** if it is empty (`""`), `"null"`, `"N/A"`, or `None`.
                        - If a required field exists but contains **invalid data**, the condition must be **NOT met**.

                        3. **Use Semantic Matching for Field Names:**
                        - Match fields based on **meaning, not exact words**.
                        - Use **fuzzy matching** to detect variations like:
                            - `"benefitCode"` ≈ `"benefit_code"`, `"benefit identifier"`, `"coverage code"`
                            - `"paymentIndicator"` ≈ `"pay_status"`, `"payment_flag"`
                        - Ensure the AI finds **the best matching field** dynamically.

                        4. **Strict Condition Evaluation:**
                        - If **ANY** required field **fails**, mark the condition as **NOT met**.
                        - If **ALL** relevant fields pass, mark the condition as **met**.

                        5. **Return Output in Strict JSON Format:**
                        ```json
                        {{"condition_name": "condition met or not and reason in few words"}}.
                        6. **Dont give entire analysis sumamry give only short summary weather condition met or not
                        '''
                        

            return self.llm.predict(prompt)

        
