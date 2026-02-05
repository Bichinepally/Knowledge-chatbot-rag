import json

print("===== TRIPLE CREATION STARTED =====")

# Load relationships
with open("relationships.json", "r", encoding="utf-8") as f:
    relationships = json.load(f)

triples = []

for r in relationships:
    triples.append({
        "subject": r.get("subject", r.get("entity")),
        "predicate": r["relation"],
        "object": r["object"]
    })

# Save triples
with open("triples.json", "w", encoding="utf-8") as f:
    json.dump(triples, f, indent=4)

print("triples.json created")
print("===== TRIPLE CREATION COMPLETED =====")