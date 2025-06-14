restaurant_document = {
  "restaurant_id": "R001",
  "name": "Oxford All-Organic Restaurant",
  "address": {
    "address": "123 High Street",
    "city": "Oxford",
    "country": "UK"
  },
  "opening_time": "2025-06-14T08:00:00Z",
  "closing_time": "2025-06-14T22:00:00Z"
}

# These are the MongoDB design patterns used in the restaurant.json file:
# 1. Attribute Pattern: The Attribute Pattern is used by embedding the address as a subdocument.

# Alternative design would be to keep a separate collection for addresses,
#  which would allow for more flexibility in querying and updating addresses.

#  Pros
# Reusability: If multiple restaurants share the same address (e.g., chains, food courts), you avoid duplication.
# Separation of Concerns: Address data can be managed and updated independently.
# Smaller Restaurant Documents: Keeps the main restaurant document smaller, especially if addresses are complex.
# Cons
# Requires Joins: To get full restaurant info with address, you need to perform an additional query (join).
# More Complex Writes: When creating or updating a restaurant, you must manage two collections.
# Potential Overhead: If addresses are rarely shared or changed, the benefit may not outweigh the added complexity.