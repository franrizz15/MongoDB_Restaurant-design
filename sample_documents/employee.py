employee_document = {
    "employee_id": 1,
    "name": "Dragos",
    "contact_info": {
      "phone": "phone1",
      "email": "email1"
    },
    "qualifications": [
      {
        "type": "academic",
        "value": "q1",
        "start_date": "01/01/2025",
        "end_date": ""

      },
      {
        "type": "professional",
        "value": "q2",
        "status": "Completed",
        "start_date": "01/01/2024",
        "expiry_date": "01/01/2026"
      }
    ]
  } 

  # These are the MongoDB design patterns used in the employee.json file:
  # 1. Attribute Pattern: The Attribute Pattern is used by embedding the contact_info as a subdocument. 
  # The qualifications array contains subdocuments with various attributes (type, value, etc.).
  # 2. Polymorphic Pattern: The qualifications array holds different types of qualifications 
  # (e.g., "academic", "professional"), each with its own set of fields. 