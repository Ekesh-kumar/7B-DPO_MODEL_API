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
        self.llm = ChatOpenAI(model_name="gpt-4-turbo", openai_api_key=openai_api_key)

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
                                You are an intelligent mainframe terminal agent that **ONLY returns JSON output** based on the following rules.

                                ### **Step 1: Immediate Check**
                                - The process check result is: "{check}"
                                - If {check}.strip().lower() == "true", proceed to Step 2.

                                - Else If {check}.strip().lower() == "false", return:
                                ```json
                                {{ "Type": "Action not possible" }}
                                ```
                                - **Do not proceed further.**

                                ### **Step 2: Validate Process Conditions**
                                - If `{process_analysis_results}` contains any failed conditions, return:
                                ```json
                                {{ "Type": "Deny Claims", "Reason": "{process_analysis_results}" }}
                                ```
                                - **Do not proceed further.**
                                - If all conditions pass, proceed to Step 3.

                                ### **Step 3: Task Execution (Generate Actions)**
                                - **Navigation and Key Retrieval**:
                                - If asked to **go to an option** (e.g., "Go to View"), first find the corresponding key (e.g., `"V"`).
                                - Return:
                                ```json
                                {{ "Type": "Type", "Value": "extracted_key" }}
                                ```
                                - If the **option name is ambiguous**, choose the **best available match** from the screen.

                                - **Entering Username and Password**:
                                - Identify fields **near "username" and "password"** on the screen.
                                - **Check existing values** in these fields:
                                    - If the username & password **already match** the given credentials, **skip entering them** and proceed to the next task.
                                    - If fields **are empty or different**, enter them in this order:
                                    ```json
                                    [
                                        {{ "Type": "Input", "Value": "username" }},
                                        {{ "Type": "KeyPress", "Value": "Enter" }},
                                        {{ "Type": "Input", "Value": "password" }}
                                    ]
                                    ```

                                - **Extracting Field Values**:
                                - If asked to retrieve a specific field's value (e.g., "Get Order ID"), return:
                                ```json
                                {{ "Type": "Value", "Value": "extracted_field_value" }}
                                ```

                                - **Ensure Proper Action Formatting**:
                                - If a task requires multiple steps, return a **JSON array**:
                                    ```json
                                    [
                                    {{ "Type": "Action 1" }},
                                    {{ "Type": "Action 2" }}
                                    ]
                                    ```
                                - **DO NOT** explain the actions—strictly return the JSON output.
                                '''
                            )





        return navigator.naviagte(response)

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

        
