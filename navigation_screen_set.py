
class navigation_set :

    def __init__(self) :

        self.navigations = {"login_to_eldorado" : {
             "conditions": [],
             "steps" : [ "1. Select Options for HEALTHPAC 4.0 Production. ", "2. Login into Health pack systems. with username ben23, and credential pip43#",
             "3. Check if the screen contains ELIG, else redirect to login screen", "4. Select Access workflow in selection list.", "5. Make sure you are in a CLAIMS HISTORY - HCS CORRECTIONAL MGMT WELLPATH screen, if yes click on '\' ",
             "6. In the CLAIMS HISTORY - HCS CORRECTIONAL MGMT WELLPATH screen find the key for Find, and click the keyboard key."] ,
             "screens" : ["start_screen", "login_screen", "Hcs_process_screen", "login_screen", "Hcs_process_screen", "parient_screen", "patient_with_menu_screen"]
            },
           
           "Find_image_name" : {
                    "conditions":[
                     


                    ],
                     "steps" : ['''Objective:
                   Task Execution Steps:

                    Step 1: Identify if the current screen is the "Claim Details" screen.
                        If confirmed, type V to navigate to claim details.

                    Step 2: Once inside the claim details screen, type O to access "Original Claim Information."

                    Step 3: Type "O" again the Claims Adjudication screen.

                    Step 4: Type A to load the image in the Claims Adjudication screen"

                    Step 5: Type X to access "Extra Claims Information."

                    Step 6: Extract the TIFF Image Name displayed on the screen.

                    Step 7: Print the TIFF Image Name.

                    Step 8: Confirm that all steps have been completed.
               '''],
             "screens" : ["claim_info_screen", "claim_processing_options", "image_claim_screen"]
           } ,
          
          "process_claims": {
             "steps" : [
                "type Y and press Enter"
             ] 
             , 
            "screens" : ["patient_claim_screen"]
            ,
            "conditions" : [
              '''
              ** "benefitCode" should be  780  for all the benefitCode then go for further process, otherwise deny the claim.
              ** If paymentIndicator maches with Alphabet P then only proceed further for claim.
              '''
            ]
          } ,

          "login_and_view_queue" : {
            "steps" : [ '''Perform the following steps to navigate the mainframe system and reach the claim information screen:

                            1. **start_screen**
                              - Select option for HEALTHpac 4.0 Production.
                              - Press Enter to confirm.

                            2. **login_screen**
                              - Check if fields for USERCODE and PASSWORD are present.
                              - Enter the following credentials:
                                - Username: MDODD1
                                - Password: Citris@123
                              - Press Enter to log in.

                            3. **Hcs_process_screen**
                              - Select the Work Flow Queue option.
                              - Press Enter to proceed.

                            4. **work_flow_screen**
                              - Select the option for 'Access Work Flow Queues'.
                              - Press Enter to confirm.

                            5. **queues_screen**
                              - Identify the option for the 'CCH-ARDOC' queue.
                              - Type the queue option.
                              - Press Enter to access the queue.

                            6. **patient_claim_screen**
                              - extract patient address.

                            Ensure that each step is executed sequentially and confirm the expected result before proceeding to the next step.
                            '''
                          ],
            "screens" : ["start_screen", "login_screen", "Hcs_process_screen" , "work_flow_screen" , "queues_screen", "patient_claim_screen" ],
             
            "conditions" : ["no conditions for this task, proceed to further step"]
              
          }
        }

    def get_navigation(self, process_id) :
        return  self.navigations.get(process_id)      