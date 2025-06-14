employee_current_document = {
  "employee_id": 1,
  "start_date": "2024-01-01",
  "job_title": "Chef",
  "restaurant_id": "R001"
}

#
# current career info could be in the employee.json file, 
#The pro is that it is easier to query the current info about an employee as it is stored
# in the same document. The con is that if an employee changes their current career frequently,
# there will be a lot of updates to the employee document, which could lead to performance issues.
# It is harder to query all current careers across employees.

