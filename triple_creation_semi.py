import json

INPUT_FILE = "relationships_semi.json"
OUTPUT_FILE = "triples_semi.json"

print("===== FIXING SEMI-STRUCTURED TRIPLES STARTED =====")

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    relationships = json.load(f)

triples = []

for r in relationships:
    subject = r.get("entity") or r.get("subject")
    predicate = r.get("relation") or r.get("predicate")
    obj = r.get("object")

    if subject and predicate and obj:
        triples.append({
            "subject": subject,
            "predicate": predicate,
            "object": obj
        })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(triples, f, indent=4)

print("triples_semi.json created successfully")
print("===== FIXING COMPLETED =====")