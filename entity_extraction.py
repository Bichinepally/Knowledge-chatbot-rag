import json

print("===== ENTITY EXTRACTION STARTED =====")

# Load normalized structured data
with open("structured_normalized.json", "r") as f:
    data = json.load(f)

entities = []

for row in data:
    entities.append({
        "entity_type": "Employee",
        "entity_value": row["name"]
    })
    entities.append({
        "entity_type": "Department",
        "entity_value": row["department"]
    })

print("Entities Extracted Successfully")

# Remove duplicates
unique_entities = { (e["entity_type"], e["entity_value"]) : e for e in entities }
entities = list(unique_entities.values())

# Save entities
with open("entities.json", "w") as f:
    json.dump(entities, f, indent=4)

print("entities.json created")
print("===== ENTITY EXTRACTION COMPLETED =====")