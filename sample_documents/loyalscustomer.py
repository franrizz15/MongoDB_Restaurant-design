loyal_customer_document = {
  "customer_id": "C001",
  "name": "Alice Smith",
  "email": "alice@example.com",
  "phone": "123-456-7890",
  "loyalty_start_date": "2022-01-01",
  "discount": 0.15,
  "restaurant_id": "R001"
}

discount = {
  "update_date": "2025-06-01",
  "max_discount": 0.20
}

# Alternatively we could use the bucket pattern for the dicount threshold relation
# {
# "year": 2025,
# "thresholds": [
#     { "update_date": "2025-06-01", "max_discount": 0.20 },
#     { "update_date": "2025-01-01", "max_discount": 0.18 }
# ]
# }

# Pros
# Efficient Reads: Fetching all related records (e.g., all discount thresholds 
# for a year) requires only one document read.
# Reduced Document Count: Fewer documents in the collection, which can improve 
# index and storage efficiency.
# Logical Grouping: Related data is grouped together, making it easier to 
# manage and archive.
# Cons
# Document Size Limit: Buckets can grow large and may eventually hit MongoDB’s 
# 16MB document size limit.
# Update Complexity: Adding or removing items from a bucket requires updating 
# the whole document, 
# which can cause contention or performance issues with frequent writes.
# Difficult Partial Updates: Updating a single item inside a large array 
# can be less efficient than updating a standalone document.
# Query Limitations: Querying for a specific item inside a bucket may be 
# less efficient than querying individual documents.
