ingredient_document = {
    "ingredient_id": "I001",
    "name": "Tomato"
}
# Pattern: Attribute Pattern (simple attributes)

food_supplier_document = {
    "supplier_id": "S001",
    "name": "Fresh Farms Ltd.",
    "address": {
        "street": "45 Green Lane",
        "city": "Oxford",
        "country": "UK"
    },
    "email": "contact@freshfarms.co.uk",
    "phone": "+44 1234 567890"
}
# Pattern: Attribute Pattern (all fields as attributes, address as embedded subdocument)

restaurant_supplier_document = {
    "restaurant_id": "R001",
    "restaurant_name": "Oxford All-Organic Restaurant",
    "supplier_id": "S001",
    "supplier_name": "Fresh Farms Ltd.",                
    "ingredient_id": "I001",
    "ingredient_name": "Tomato",                        
    "start_date": "2025-01-01",
    "end_date": "2025-12-31",
    "max_quantity": 100,
    "unit_cost_pounds": 2.5
}
# Pattern: Extended Reference Pattern + Subset Pattern (for names)
# Pattern: Extended Reference Pattern (references to restaurant, supplier, ingredient)

restaurant_order_document = {
    "order_id": "O001",
    "restaurant_id": "R001",
    "restaurant_name": "Oxford All-Organic Restaurant",  # Subset Pattern
    "supplier_id": "S001",
    "supplier_name": "Fresh Farms Ltd.",                # Subset Pattern
    "ingredient_id": "I001",
    "ingredient_name": "Tomato",                        # Subset Pattern
    "order_date": "2025-06-14",
    "quantity": 50,
    "status": "Delivered"
}
# Pattern: Extended Reference Pattern + Subset Pattern (for names)
# Pattern: Extended Reference Pattern (references to restaurant, supplier, ingredient)

restaurant_ingredients_source_document = {
    "restaurant_id": "R001",
    "restaurant_name": "Oxford All-Organic Restaurant",  
    "supplier_id": "S001",
    "supplier_name": "Fresh Farms Ltd.",                
    "ingredient_id": "I001",
    "ingredient_name": "Tomato",                        
    "dish_id": "D001",
    "dish_name": "Margherita Pizza",                    
    "date": "2025-06-14"
}
# Pattern: Extended Reference Pattern + Subset Pattern (for names)
# Pattern: Extended Reference Pattern (references to restaurant, supplier, ingredient, dish)

dish_served_document = {
    "restaurant_order_id": "O001",
    "dish_id": "D001",
    "restaurant_id": "R001",
    "date": "2025-06-14",
    "loyal": True
}
# Pattern: Extended Reference Pattern (references to order, dish, restaurant)