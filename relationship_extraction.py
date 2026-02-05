import json

print("===== RELATIONSHIP EXTRACTION STARTED =====")

# Load normalized data
with open("structured_normalized.json", "r") as f:
    data = json.load(f)

relationships = []

for row in data:
    relationships.append({
        "subject": row["name"],
        "relation": "works_in",
        "object": row["department"]
    })

    relationships.append({
        "subject": row["name"],
        "relation": "has_salary",
        "object": row["salary"]
    })

    relationships.append({
        "subject": row["name"],
        "relation": "has_experience",
        "object": row["experience_years"]
    })

# Save relationships
with open("relationships.json", "w") as f:
    json.dump(relationships, f, indent=4)

print("relationships.json created")
print("===== RELATIONSHIP EXTRACTION COMPLETED =====")