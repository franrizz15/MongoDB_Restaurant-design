restaurant_document = {
  "restaurant_id": "R001",
  "name": "Oxford All-Organic Restaurant",
  "address": {
    "address": "123 High Street",
    "city": "Oxford",
    "country": "UK"
  },
  "hours": {
    "Monday":    {"open": "08:00", "close": "22:00"},
    "Tuesday":   {"open": "08:00", "close": "22:00"},
    "Wednesday": {"open": "08:00", "close": "22:00"},
    "Thursday":  {"open": "08:00", "close": "22:00"},
    "Friday":    {"open": "08:00", "close": "23:00"},
    "Saturday":  {"open": "09:00", "close": "23:00"},
    "Sunday":    {"open": "11:00", "close": "21:00"}
  }
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