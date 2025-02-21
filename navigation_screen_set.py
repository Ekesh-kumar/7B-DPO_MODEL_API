
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
          } 
        }

    def get_navigation(self, process_id) :
        return  self.navigations.get(process_id)      