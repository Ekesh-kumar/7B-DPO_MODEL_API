import json


class Summary_json_agent:

    def __init__(self) :
            
            self.screen_analysis =   {
                "start_screen":
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
                },

                "login_screen":  {
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
                    },

                "login_screen_with_cred" :
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
                },

            "Hcs_process_screen": {
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
                } ,
            "patient_screen": {
                "window_name": "CLAIMS HISTORY - HCS CORRECTIONAL MGMT WELLPATH",
                "group": {
                    "id": "263 790263",
                    "name": "BROWN COUNTY JAIL",
                    "status": {
                    "paid": "Never",
                    "effect_date": "01/01/18",
                    "termed_date": "N/A"
                    }
                },
                "employee_info": {
                    "address": "3030 CURRY ST, GREEN BAY, WI 54311",
                    "ssn": "920-31-0634",
                    "birthday": "11/12/88",
                    "age": 34,
                    "sex": "M",
                    "certificate": "930000026255",
                    "medical_und": "No",
                    "takeover": "No",
                    "cob": "No"
                },
                "remarks": "",
                "patient_info": "The Patient is the Employee, shown above.",
                "coverage": {
                    "medical": [
                    {
                        "date": "09/10/22",
                        "status": "TERMED"
                    },
                    {
                        "date": "02/20/22",
                        "status": "ACTIVE",
                        "id": "790263A"
                    },
                    {
                        "date": "02/17/22",
                        "status": "TERMED"
                    }
                    ],
                    "dental": [
                    {
                        "date": "09/10/22",
                        "status": "TERMED"
                    },
                    {
                        "date": "02/20/22",
                        "status": "ACTIVE",
                        "id": "790263A"
                    },
                    {
                        "date": "02/17/22",
                        "status": "TERMED"
                    }
                    ]
                },
                "navigation": "Press Tab key to view other products",
                "confirmation_prompt": "Is selection correct?"
                },
                
               "patient_with_menu_screen": {
                "window_name": "CLAIMS ADJUDICATION - HCS CORRECTIONAL MGMT WELLPATH",
                "group": {
                    "id": "263 790263",
                    "name": "BROWN COUNTY JAIL",
                    "status": {
                    "paid": "Never",
                    "effect_date": "01/01/18",
                    "termed_date": "N/A"
                    }
                },
                "employee_info": {
                    "address": "3030 CURRY ST, GREEN BAY, WI 54311",
                    "ssn": "920-31-0634",
                    "birthday": "11/12/88",
                    "age": 34,
                    "sex": "M",
                    "certificate": "930000026255",
                    "medical_und": "No",
                    "takeover": "No",
                    "cob": "No"
                },
                "remarks": "",
                "patient_info": "The Patient is the Employee, shown above.",
                "coverage": {
                    "medical": [
                    {
                        "date": "09/10/22",
                        "status": "TERMED"
                    },
                    {
                        "date": "02/20/22",
                        "status": "ACTIVE",
                        "id": "790263A"
                    },
                    {
                        "date": "02/17/22",
                        "status": "TERMED"
                    }
                    ],
                    "dental": [
                    {
                        "date": "09/10/22",
                        "status": "TERMED"
                    },
                    {
                        "date": "02/20/22",
                        "status": "ACTIVE",
                        "id": "790263A"
                    },
                    {
                        "date": "02/17/22",
                        "status": "TERMED"
                    }
                    ]
                },
                "navigation": "Press Tab key to view other products",
                "selection_prompt": "SELECT:",
                "available_options": {
                    "M": "Main",
                    "P": "Prior",
                    "R": "Resume",
                    "F": "Find",
                    "H": "History",
                    "U": "Utilities",
                    "L": "Plan"
                }
            },

            "patient_claim_screen" : '''
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
                ,
                "claim_processing_options":  
                                ''' "title": "Select Details to View",
                                    "available_options": {
                                        "D": "Diagnosis Information",
                                        "S": "Service Line Details",
                                        "M": "Master File Details",
                                        "H": "Claims History",
                                        "C": "Payment Information",
                                        "T": "Tooth Chart",
                                        "I": "Claim Image",
                                        "N": "Claim Notes",
                                        "O": "Original Claim Information",
                                        "W": "Patient Episode Information",
                                        "A": "Audit History of Claim",
                                        "Y": "Summary Screen"
                                    },
                                    "unavailable_options": [
                                        "n/a",
                                        "n/a"
                                    ]''',

                "image_claim_screen" :
                        '''
                        "claim_information": {
                        "claim_number": "222-483371-00",
                        "status_of_claim": "PDC 11/09/22 KARRIE",
                        "received_date": "11/04/22",
                        "incurred_date": "10/22/22",
                        "plan_id": "790216A",
                        "effective_date": "02/01/17"
                    },
                    "repricing_details": {
                        "repricing_method": "External sent EDI",
                        "icd_code": "S01.01XA",
                        "und_group_codes": [
                            "790",
                            "790216"
                        ],
                        "network": "CMA",
                        "claim_source": "EDI 11/07/22"
                    },
                    "billing_details": [
                        {
                            "from_dos": "10/22/22",
                            "proceed": null,
                            "units": null,
                            "charge_amount": null,
                            "discount_amount": null,
                            "repriced_amount": null,
                            "oi_paid": 0.0
                        },
                        {
                            "from_dos": "10/22/22",
                            "proceed": null,
                            "units": null,
                            "charge_amount": null,
                            "discount_amount": null,
                            "repriced_amount": null,
                            "oi_paid": 0.0
                        }
                    ],
                    "additional_claims_information": {
                        "tiff_image_name": "110322751469229",
                        "external_claim_id": null,
                        "alternate_claim_id": null
                    },
                    "claim_totals": {
                        "total_charge_amount": 1775.0,
                        "total_discount_amount": 0.0,
                        "total_repriced_amount": 1775.0,
                        "total_oi_paid": 0.0
                    },
                    "provider_information": {
                        "patient_tax_id": "256023455",
                        "provider_tax_id": "593677604",
                        "employee_patient": "YATES, THOMAS (Self)",
                        "provider_name": "TAMPA BAY EMERGENCY PHYSICIANS LLC"
                    },
                    "status_indicators": {
                        "image_available": true,
                        "claim_notes_available": true
                    },
                    "navigation_options": {
                        "G": "Go Back",
                        "R": "Resume"
                    }'''
            }
            
            
    def get_screen(self, screen_name) :
        return self.screen_analysis.get(screen_name)