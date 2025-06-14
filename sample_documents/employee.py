employee_document = {
  "employee_id": "E001",
  "name": "Jane Doe",
  "contact": {"email": "jane@allorganic.com", "phone": "123456789"},

    "qualifications": [
      {
        "type": "academic",
        "value": "Nutritional Sciences BSc",
        "start_date": "01/01/2020",
        "end_date": "01/01/2023"

      },
      {
        "type": "professional",
        "value": "CTH",
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