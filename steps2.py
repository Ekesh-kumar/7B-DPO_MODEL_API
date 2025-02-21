from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import openai
import dotenv
import os

dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

mainframe_menu_prompt = """
Mainframe System Menu:

1. Customer Management
    1.1 Add New Customer
        Fields: Customer ID (editable), First Name (editable), Last Name (editable), Address (editable)
    1.2 Update Customer Information - U
        1.2.1 Search Customer
            Fields: Customer ID (editable)
            Actions: more (to view more fields)
                Fields: Last Name, Phone #
            Actions: Retrieve Customer Data
        1.2.2 Update Customer Details
            Fields: First Name (editable), Last Name (editable), Address (editable), Contact Number (editable)
    1.3 Delete Customer
        Fields: Customer ID (editable)

2. Claims Processing
    2.1 Create New Claim
        Fields: Claim ID (editable), Customer ID (editable), Claim Amount (editable)
    2.2 View/Update Claim
        2.2.1 Search Claim by ID
            Fields: Claim ID (editable)
            Actions: Retrieve Claim Data
        2.2.2 Update Claim Details
            Fields: Claim Status (editable),  Customer ID (editable), Claim Amount (editable)
        2.2.3 Delete Claim
            Fields: Claim ID (editable)
    2.3 Process Claim Payment

3. Reports
    3.1 Customer Report
    3.2 Claims Report

4. System Administration
    4.1 User Management
    4.2 System Configuration


5. claim screen 
   {
    "claim_number": "222-483371-00",
    "status_of_claim": "PAID",
    "date_paid": "11/15/22",
    "received_date": "11/04/22",
    "incurred_date": "10/22/22",
    "plan_id": "790216A",
    "effective_date": "02/01/17",
    "diagnosis": {
        "description": "Open wound of h",
        "icd_code": "S01.01XA",
        "year": 2022
    },
    "group_codes": [
        "790",
        "790216"
    ],
    "network": "CMA",
    "claim_source": "EDI 11/07/22",
    "benefits": [
        {
            "ben": 780,
            "from_dos": "10/22/22",
            "visit": 1,
            "charge_amount": 1025.0,
            "disallowed": 1025.0,
            "deductible": 0.0,
            "pct": 0,
            "payment": 0.0
        },
        {
            "ben": 780,
            "from_dos": "10/22/22",
            "visit": 1,
            "charge_amount": 750.0,
            "disallowed": 750.0,
            "deductible": 0.0,
            "pct": 0,
            "payment": 0.0
        }
    ],
    "total_charge_amount": 1775.0,
    "total_disallowed": 1775.0,
    "total_deductible": 0.0,
    "total_payment": 0.0,
    "adjustments": {
        "adj": 0.0,
        "cob_adj": 0.0,
        "withhold": 0.0,
        "total": 0.0
    },
    "provider_info": {
        "tax_id": "593677604",
        "employee_patient_provider": "(Self)",
        "provider_name": "TAMPA BAY EMERGENCY PHYSICIANS"
    },
    "net_payment": 0.0,
    "claim_notes_exist": true
}

"""

def generate_navigation_steps(intent, menu_structure):



    """Generates the single best navigation path as a list of strings."""

    navigation_prompt_template = """
    You are an AI agent designed to generate navigation steps for a mainframe system. 
    Given a user intent and the mainframe menu structure, your task is to generate the 
    SINGLE BEST sequence of steps required to accomplish the task.  Do NOT execute 
    the steps. Just list them.

    Mainframe Menu Structure:
    {menu_structure}

    User Intent: {intent}

    Generate the navigation steps as a numbered list.  Each step should be a complete 
    instruction.  Include any necessary data input (like Customer ID) in the steps.

    Prioritize paths that directly relate to the user's intent.  Avoid irrelevant 
    menu options.  For example, if the user wants to "view claims," do not include 
    steps related to "delete claims."
    
    
    Example:
    User Intent: View claims of customer whose claim id is 4490
    Navigation Steps:
    1. Navigate to: 2. Claims Processing -> 2.2 View/Update Claim -> 2.2.1 Search Claim by ID
    2. Enter Claim ID: 4490
    3. Retrieve Claim Data

    Begin!
    """
    NAVIGATION_PROMPT = PromptTemplate(
        input_variables=["menu_structure", "intent"],
        template=navigation_prompt_template,
    )

    final_prompt = NAVIGATION_PROMPT.format(menu_structure=menu_structure, intent=intent)

    llm = OpenAI(temperature=0)  # Initialize LLM here. Make sure you have your OpenAI key set in environment variables
    steps_string = llm(final_prompt)

    steps = []
    for line in steps_string.strip().split('\n'):
        if line:
            try:
                step_number, step_instruction = line.split('.', 1)  # Split by first '.'
                steps.append(step_instruction.strip())
            except ValueError:
                print(f"Warning: Could not parse step: {line}")
    return steps


def execute_steps(steps):
    """Executes the navigation steps (PLACEHOLDER - IMPLEMENT YOUR MAINFRAME INTERACTION HERE)."""
    for step in steps:
        print(f"Executing: {step}")
        # ***REPLACE THE FOLLOWING WITH YOUR ACTUAL MAINFRAME AUTOMATION CODE***
        if "Navigate to" in step:
            path = step.split("Navigate to:")[1].strip()
            print(f"Navigating to: {path}")  # Replace with actual navigation code (e.g., using pyautogui)
        elif "Enter Customer ID" in step:
            customer_id = step.split("Enter Customer ID:")[1].strip()
            print(f"Entering Customer ID: {customer_id}") # Replace with actual data entry code
        elif "Retrieve Customer Data" in step:
            print("Retrieving Customer Data") # Replace with actual data retrieval code
        elif "Enter New Last Name" in step:
            new_last_name = step.split("Enter New Last Name:")[1].strip()
            print(f"Entering new last name: {new_last_name}") # Replace with actual data entry code
        # ... Add more conditions for other types of steps ...
        else:
            print(f"Unknown step type: {step}") # Handle unknown steps

process_prompt = "pending"

while True:
    print("Tell me what to do")
    intent = input()

    if intent == 'x':
        break
    
    # user_intent = "Update customer last name to Smith of customer ID 12345"
    # navigation_steps = generate_navigation_steps(user_intent, mainframe_menu_prompt)
    
    user_intent = intent
    navigation_steps = generate_navigation_steps(user_intent, mainframe_menu_prompt)

    print("Navigation Steps:")
    for i, step in enumerate(navigation_steps):
        print(f"{i+1}. {step}")

    # execute_steps(navigation_steps)  # Execute the generated steps