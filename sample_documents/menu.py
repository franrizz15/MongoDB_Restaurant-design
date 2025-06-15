dish_document = {
  "dish_id": "D001",
  "name": "Margherita Pizza"
}

menu_document = {
  "menu_id": "M001",
  "start_date": "2025-01-01",
  "end_date": "2025-06-30",
  "dishes": [
    { "dish_id": "D001", "name": "Margherita Pizza" },
    { "dish_id": "D002", "name": "Pepperoni Pizza" }
  ]
}


# These are the MongoDB design patterns used in the menu.json file:
# Subset/Extended Reference Pattern: The dishes array references dish IDs. 
# This is a subset of the full dish documents and uses references instead of embedding full dish details.

# Alternatives
# If you want to track additional info per menu item (e.g., price, availability), use a separate collection for Menu.
# Use the Menu schema with a dishes array for most cases (efficient for reading a menu).
# Use a separate MenuItems collection if you need to store extra info per menu-dish relationship.