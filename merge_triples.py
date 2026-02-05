import json

all_triples = []

files = [
    "triples_structured.json",
    "triples_semi.json",
    "triples_unstructured.json"
]

for file in files:
    with open(file, "r") as f:
        data = json.load(f)
        all_triples.extend(data)

with open("triples.json", "w") as f:
    json.dump(all_triples, f, indent=2)

print("✅ All triples merged into triples.json")