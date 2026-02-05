import json

print("=== UNSTRUCTURED RELATIONSHIP EXTRACTION STARTED ===")

with open("unstructured_normalized.json", "r") as f:
    data = json.load(f)

relationships = []

aspects = ["product", "delivery", "price", "experience"]
sentiments = ["bad", "average", "good", "excellent", "poor"]

for row in data:
    text = row.get("text", "").lower()

    for aspect in aspects:
        if aspect in text:
            for sentiment in sentiments:
                if sentiment in text:
                    relationships.append({
                        "entity": aspect,
                        "relation": "has_sentiment",
                        "object": sentiment
                    })

# Remove duplicates
relationships = list({
    (r["entity"], r["relation"], r["object"]): r
    for r in relationships
}.values())

with open("relationships_unstructured.json", "w") as f:
    json.dump(relationships, f, indent=4)

print("relationships_unstructured.json created successfully")
print("=== UNSTRUCTURED RELATIONSHIP EXTRACTION COMPLETED ===")