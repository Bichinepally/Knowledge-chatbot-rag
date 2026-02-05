import json
import ast

print("=== SEMI-STRUCTURED RELATIONSHIP EXTRACTION STARTED ===")

with open("semi_structured_normalized.json", "r") as f:
    data = json.load(f)

relationships = []

for row in data:
    event_data_str = row.get("event_data")

    # Convert string to dict if required
    if isinstance(event_data_str, str):
        event_data = ast.literal_eval(event_data_str)
    else:
        event_data = event_data_str

    user_id = event_data.get("User_Id")
    event = event_data.get("Event")

    metadata = event_data.get("Metadata", {})
    product = metadata.get("Product")
    transaction = metadata.get("Transaction")

    # User → Event
    if user_id and event:
        relationships.append({
            "subject": f"User_{user_id}",
            "relation": "performed_event",
            "object": event
        })

    # User → Product
    if user_id and product:
        relationships.append({
            "subject": f"User_{user_id}",
            "relation": "interacted_with",
            "object": product
        })

    # Event → Transaction
    if event and transaction:
        relationships.append({
            "subject": event,
            "relation": "has_status",
            "object": transaction
        })

with open("relationships_semi.json", "w") as f:
    json.dump(relationships, f, indent=4)

print("relationships_semi.json created successfully")
print("=== SEMI-STRUCTURED RELATIONSHIP EXTRACTION COMPLETED ===")