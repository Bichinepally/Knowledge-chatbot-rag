import json
import ast

print("=== SEMI-STRUCTURED ENTITY EXTRACTION STARTED ===")

with open("semi_structured_normalized.json", "r") as f:
    data = json.load(f)

entities = []

for row in data:
    # event_data is a STRING → convert to dict
    event_data_str = row.get("event_data")

    if isinstance(event_data_str, str):
        event_data = ast.literal_eval(event_data_str)
    else:
        event_data = event_data_str

    user_id = event_data.get("User_Id")
    event = event_data.get("Event")

    metadata = event_data.get("Metadata", {})
    product = metadata.get("Product")
    transaction = metadata.get("Transaction")

    if user_id is not None:
        entities.append({
            "entity_type": "User",
            "entity_value": f"User_{user_id}"
        })

    if event:
        entities.append({
            "entity_type": "Event",
            "entity_value": event
        })

    if product:
        entities.append({
            "entity_type": "Product",
            "entity_value": product
        })

    if transaction:
        entities.append({
            "entity_type": "Transaction",
            "entity_value": transaction
        })

# Remove duplicates
entities = list({(e["entity_type"], e["entity_value"]): e for e in entities}.values())

with open("entities_semi.json", "w") as f:
    json.dump(entities, f, indent=4)

print("entities_semi.json created successfully")
print("=== SEMI-STRUCTURED ENTITY EXTRACTION COMPLETED ===")