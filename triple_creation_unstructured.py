import json

print("=== UNSTRUCTURED TRIPLE CREATION STARTED ===")

with open("relationships_unstructured.json", "r") as f:
    relationships = json.load(f)

triples = []

for r in relationships:
    triples.append({
        "subject": r["entity"],
        "predicate": r["relation"],
        "object": r["object"]
    })

with open("triples_unstructured.json", "w") as f:
    json.dump(triples, f, indent=4)

print("triples_unstructured.json created successfully")
print("=== UNSTRUCTURED TRIPLE CREATION COMPLETED ===")