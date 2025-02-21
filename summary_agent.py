import json


class Summary_json_agent:

    def __init__(self) :
            
            self.screen_analysis =   {
                "start_screen":
                '''start_screen:
                {
                    "system_information": {
                        "operating_system": "CentOS 6.10 (Final) (x86_64)",
                        "user": "lfrancel",
                        "password_expiry": "Never"
                    },
                    "menu_title": "HEALTH COST SOLUTIONS",
                    "menu_options": {
                        "1 - HEALTHpac_4.0_Production": "Likely the main application for production use.",
                        "2 - HEALTHpac_4.0_Test": "A testing environment for the application.",
                        "88 - Change_Password": "Allows the user to update their password.",
                        "99 - Logout": "Ends the session and logs the user out."
                    },
                    "user_interaction": {
                        "system_prompt": "Enter selection please >",
                        "required_action": "Give the option required for selecting desired functionality."
                    }
                }''',

                "login_screen":  '''
                    login_screen:
                    {
                    "window_name": "Healthpac Systems - Eldorado Computing, Inc.",
                    "release_version": "4.21.01",
                    "main_sections": [
                        {
                        "title": "Healthpac IV - Health Care Management System",
                        "subtext": [
                            "Health Cost Solutions, Inc.",
                            "A Division of MPHASIS Inc."
                        ]
                        },
                        {
                        "title": "Login Section",
                        "prompt": "PLEASE LOG INTO THE SYSTEM",
                        "input_fields": [
                            {
                            "name": "Usercode",
                            "type": "text"
                            },
                            {
                            "name": "Password",
                            "type": "password"
                            }
                        ]
                        }
                    ],
                    "footer": "(c) Copyright 2003 - Eldorado Computing, Inc. All Rights Reserved"
                    }''',

                "login_screen_with_cred" :
                '''login_screen_with_cred:
                  {
                    "window_name": "Healthpac Systems - Eldorado Computing, Inc.",
                    "release_version": "4.21.01",
                    "main_sections": [
                    {
                        "title": "Healthpac IV - Health Care Management System",
                        "subtext": [
                        "Health Cost Solutions, Inc.",
                        "A Division of MPHASIS Inc."
                        ]
                    },
                    {
                        "title": "Login Section",
                        "prompt": "PLEASE LOG INTO THE SYSTEM",
                        "input_fields": [
                        {
                            "name": "Usercode",
                            "type": "text",
                            "value": "LFRANC"
                        },
                        {
                            "name": "Password",
                            "type": "password",
                            "value": "****"
                        }
                        ]
                    }
                    ],
                    "footer": "(c) Copyright 2003 - Eldorado Computing, Inc. All Rights Reserved"
                }''',

            "Hcs_process_screen": '''
               Hcs_process_screen:
               {
                "window_name": "HEALTHpac Version 4.21.01",
                "date_time": "Mon Feb 06 2023 9:21",
                "user": "LAUREN FRANCEL",
                "department": "HCS CORRECTIONAL MGMT WELLPAT",
                "main_section": {
                    "title": "HCS CCS PROCESSING",
                    "menu_options": [
                    {
                        "option_number": 1,
                        "description": "ACCESS WORKFLOW"
                    },
                    {
                        "option_number": 2,
                        "description": "CLAIMS/ELIGIBILITY"
                    },
                    {
                        "option_number": 3,
                        "description": "PROVIDER UTILITIES"
                    },
                    {
                        "option_number": 4,
                        "description": "GROUP MASTER"
                    },
                    {
                        "option_number": 5,
                        "description": "AUTHORIZATIONS"
                    },
                    {
                        "option_number": 6,
                        "description": "REPORTS"
                    },
                    {
                        "option_number": 7,
                        "description": "PRINT REPRICING SHEETS (801)"
                    },
                    {
                        "option_number": 8,
                        "description": "CHANGE UNDERWRITERS"
                    },
                    {
                        "option_number": 9,
                        "description": "LOG OFF SYSTEM"
                    }
                    ]
                },
                "footer_options": {
                    "M": "Main Menu",
                    "P": "Previous Menu",
                    "I": "Information",
                    "E": "Electronic Messages"
                },
                "input_prompt": "Enter: ______"
                }''',

            "work_flow_screen" : '''
                            work_flow_screen:
                            {
                            "screen_title": "Work Flow Queues",
                            "options": [
                                {
                                "selection": "1",
                                "description": "Access Work Flow Queues"
                                }
                            ]
                            }
                           ''',

            "queues_screen": '''
                       queues_screen:
                       {
                        "screen_title": "WORKFLOW QUEUES",
                        "header": "***SELECT***",
                        "system": "HCS CORRECTIONAL MGMT WELLPATH",
                        "queue_owner": "MDODDE'S QUEUES",
                        "columns": ["SEL", "NAME", "DESCRIPTION", "JOBS"],
                        "entries": [
                            {
                            "selection": "1",
                            "name": "CCH-790136",
                            "description": "PA DOC",
                            "jobs": "P1"
                            },
                            {
                            "selection": "2",
                            "name": "CCH-ARDOC",
                            "description": "ARDOC EFF 1/1/2020 NO BCBS",
                            "jobs": ""
                            },
                            {
                            "selection": "3",
                            "name": "CCH-CA",
                            "description": "ALL CA SITES HCFA'S",
                            "jobs": ""
                            },
                            {
                            "selection": "4",
                            "name": "CCH-CA UB",
                            "description": "ALL CA SITES UB'S",
                            "jobs": ""
                            },
                            {
                            "selection": "5",
                            "name": "CCH-MDCARE",
                            "description": "MEDICARE SITES HCFA AND UBS",
                            "jobs": ""
                            }
                        ],
                        "navigation": {
                            "instructions": "Arrow up / down",
                            "current_selection": "1",
                            "action": "Enter to access"
                        }
                        }
                        ''',

            

            "patient_claim_screen" : '''
                            patient_claim_screen:
                            {
                                "screenAnalysis": {
                                    "title": "Claim Information Screen",
                                    "overallStatus": "PEND",
                                    "claimNumber": "225-014871-00",
                                    "receivedDate": "02/18/25",
                                    "patientName": "REUBEN",
                                    "incurredDate": "01/23/25",
                                    "planId": "790136A",
                                    "effectiveDate": "02/01/17",
                                    "diagnosis": {
                                    "description": "R06 Abnormalities",
                                    "icd": "R06.02",
                                    "year": "2025",
                                    "underGroup": "790 790136",
                                    "network": "CMA",
                                    "claimSource": "EDI 02/12/25"
                                    },
                                    "benefits": [
                                    {
                                        "benefitCode": "780",
                                        "dateOfService": "01/23/25",
                                        "visit": "1",
                                        "chargeAmount": "1096.60",
                                        "disallowedAmount": "578.53",
                                        "deductibleAmount": ".00",
                                        "percentagePaid": "100",
                                        "paymentAmount": "518.07",
                                        "paymentIndicator": "P"
                                    },
                                    {
                                        "benefitCode": "789",
                                        "dateOfService": "01/23/25",
                                        "visit": "0",
                                        "chargeAmount": "172.32",
                                        "disallowedAmount": "29.56",
                                        "deductibleAmount": ".00",
                                        "percentagePaid": "100",
                                        "paymentAmount": "142.76",
                                        "paymentIndicator": "P"
                                    },
                                    {
                                        "benefitCode": "780",
                                        "dateOfService": "01/23/25",
                                        "visit": "0",
                                        "chargeAmount": "40.16",
                                        "disallowedAmount": "40.16",
                                        "deductibleAmount": ".00",
                                        "percentagePaid": "0",
                                        "paymentAmount": ".00",
                                        "paymentIndicator": "P"
                                    },
                                    {
                                        "benefitCode": "780",
                                        "dateOfService": "01/23/25",
                                        "visit": "0",
                                        "chargeAmount": "133.91",
                                        "disallowedAmount": "133.91",
                                        "deductibleAmount": ".00",
                                        "percentagePaid": "0",
                                        "paymentAmount": ".00",
                                        "paymentIndicator": "P"
                                    }
                                    ],
                                    "totals": {
                                    "totalChargedAmount": "1442.99",
                                    "totalDisallowedAmount": "782.16",
                                    "totalDeductibleAmount": ".00",
                                    "totalPaymentAmount": "660.83"
                                    },
                                    "adjustments": {
                                    "adjustmentAmount": ".00",
                                    "cobAdjustmentAmount": ".00",
                                    "withholdAmount": ".00",
                                    "totalAdjustmentAmount": ".00"
                                    },
                                    "taxId": {
                                    "patientTaxId": "997314611",
                                    "providerTaxId": "251799853"
                                    },
                                    "employeePatient": {
                                    "name": "WHITE, ALVIN / (Self)"
                                    },
                                    "provider": {
                                    "name": "SUPERIOR AMBULANCE SERVICE INC"
                                    },
                                    "checkNumber": null,
                                    "netPayment": {
                                    "patientPayment": ".00",
                                    "providerPayment": "660.83",
                                    "alternatePayeePayment": ".00",
                                    "electronicPaymentInformation": "660.83"
                                    },
                                    "imageAvailable": true,
                                    "claimNotesExist": true,
                                    "navigationOptions": {
                                    "main": "M",
                                    "prior": "P",
                                    "resume": "R",
                                    "unpend": "U",
                                    "view": "V",
                                    "options": "0",
                                    "find": "F"
                                    },
                                    "search": "Q",
                                    "time": "5:17 AM",
                                    "date": "2/18/2023"
                                }
                                }    
                            '''
            }
            
            
    def get_screen(self, screen_name) :
        return self.screen_analysis.get(screen_name)