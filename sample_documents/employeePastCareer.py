employee_past_career_document ={
  "employee_id": 1,
  "past_careers": [
    {
      "start_date": "2022-01-01",
      "end_date": "2023-12-31",
      "job_title": "Waiter",
      "restaurant_id": "R002"
    },
    {
      "start_date": "2020-01-01",
      "end_date": "2021-12-31",
      "job_title": "Chef",
      "restaurant_id": "R003"
    }
  ]
}


# These are the MongoDB design patterns used in the employeePastCareer.json file:  
# 1. Bucket Pattern: The past_careers array is used to store multiple career records for the employee,
# allowing for efficient querying of past job history.
# An alternative design would be to store the past careers in a separate collection,
# which would allow for more flexibility in querying and updating past career records.
# It requires more complex queries to join the employee with their past careers,
# but it can be more efficient for certain operations, such as retrieving all past careers across employees.