import fitz  # PyMuPDF
import os
import json

DATA_PATH = "source_docs"
triples = []

def add_triple(s, p, o):
    triples.append({"subject": s, "predicate": p, "object": o})

def process_pdf(filename, subject_name):
    path = os.path.join(DATA_PATH, filename)
    doc = fitz.open(path)

    for page_num, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            add_triple(subject_name, "contains_text_page", f"Page {page_num+1}: {text[:500]}")

# ---- PROCESS EACH PDF ----
process_pdf("Annual-Report-2024-25_unstructured.pdf", "Annual_Report")
process_pdf("employee_engagement_reports_unstructured.pdf", "Employee_Engagement_Report")
process_pdf("Infosys_Company_Details_unstructured.pdf", "Infosys_Company_Details")

# SAVE
with open("triples_unstructured.json", "w") as f:
    json.dump(triples, f, indent=2)

print("✅ Unstructured triples created successfully!")