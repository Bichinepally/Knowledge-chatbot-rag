import json
import os

DATA_PATH = "source_docs"
triples = []

def add_triple(s, p, o):
    triples.append({"subject": str(s), "predicate": str(p), "object": str(o)})

# -------- EMAIL DATA --------
with open(os.path.join(DATA_PATH, "email_data_semi structured.json")) as f:
    emails = json.load(f)

for mail in emails:
    sender = mail.get("sender", "Unknown")
    receiver = mail.get("receiver", "Unknown")
    subject = mail.get("subject", "")
    add_triple(sender, "sent_email_to", receiver)
    add_triple(sender, "email_subject", subject)

# -------- MEETING DATA --------
with open(os.path.join(DATA_PATH, "meeting_data_semi structured.json")) as f:
    meetings = json.load(f)

for meet in meetings:
    host = meet.get("host", "Unknown")
    topic = meet.get("topic", "")
    date = meet.get("date", "")
    add_triple(host, "conducted_meeting_on", topic)
    add_triple(topic, "meeting_date", date)

# -------- PERFORMANCE DATA --------
with open(os.path.join(DATA_PATH, "performance_semi structured.json")) as f:
    performance = json.load(f)

for record in performance:
    emp = record.get("employee", "Unknown")
    rating = record.get("rating", "")
    add_triple(emp, "performance_rating", rating)

# SAVE
with open("triples_semi.json", "w") as f:
    json.dump(triples, f, indent=2)

print("✅ Semi-structured triples created successfully!")