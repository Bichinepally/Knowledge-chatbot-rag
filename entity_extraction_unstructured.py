import json

print("=== UNSTRUCTURED ENTITY EXTRACTION STARTED ===")

with open("unstructured_normalized.json", "r") as f:
    data = json.load(f)

entities = []

for row in data:
    text = row.get("text", "").lower()

    # Aspect entities
    for aspect in ["product", "delivery", "price", "experience"]:
        if aspect in text:
            entities.append({
                "entity_type": "Aspect",
                "entity_value": aspect
            })

    # Sentiment entities
    for sentiment in ["bad", "average", "good", "excellent", "poor"]:
        if sentiment in text:
            entities.append({
                "entity_type": "Sentiment",
                "entity_value": sentiment
            })

# Remove duplicates
entities = list({
    (e["entity_type"], e["entity_value"]): e
    for e in entities
}.values())

with open("entities_unstructured.json", "w") as f:
    json.dump(entities, f, indent=4)

print("entities_unstructured.json created successfully")
print("=== UNSTRUCTURED ENTITY EXTRACTION COMPLETED ===")