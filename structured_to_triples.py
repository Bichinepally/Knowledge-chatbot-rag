import pandas as pd
import json
import os

DATA_PATH = "source_docs"
triples = []

def add_triple(s, p, o):
    triples.append({"subject": str(s), "predicate": str(p), "object": str(o)})

# Helper to find column safely
def get_col(df, possible_names):
    for name in possible_names:
        if name in df.columns:
            return name
    return None

# ---------------- EMPLOYEES ----------------
df = pd.read_csv(os.path.join(DATA_PATH, "employee_structured.csv"))
df.columns = df.columns.str.strip().str.lower()

id_col = get_col(df, ["employee_id", "emp_id", "id"])
name_col = get_col(df, ["name", "employee_name"])
dept_col = get_col(df, ["department", "dept"])

for _, row in df.iterrows():
    emp = f"Employee_{row[id_col]}" if id_col else "Employee_Unknown"
    if name_col:
        add_triple(emp, "name", row[name_col])
    if dept_col:
        add_triple(emp, "works_in", row[dept_col])

# ---------------- ASSETS ----------------
df = pd.read_csv(os.path.join(DATA_PATH, "assets_structured.csv"))
df.columns = df.columns.str.strip().str.lower()

asset_col = get_col(df, ["asset_id", "asset"])
emp_col = get_col(df, ["employee_id", "emp_id"])

for _, row in df.iterrows():
    if asset_col and emp_col:
        add_triple(f"Asset_{row[asset_col]}", "assigned_to", f"Employee_{row[emp_col]}")

# ---------------- ATTENDANCE ----------------
df = pd.read_csv(os.path.join(DATA_PATH, "attendance_structured.csv"))
df.columns = df.columns.str.strip().str.lower()

emp_col = get_col(df, ["employee_id", "emp_id"])
status_col = get_col(df, ["status", "attendance_status"])

for _, row in df.iterrows():
    if emp_col and status_col:
        add_triple(f"Employee_{row[emp_col]}", "attendance_status", row[status_col])

# ---------------- FINANCIALS ----------------
df = pd.read_csv(os.path.join(DATA_PATH, "company_financials_structured.csv"))
df.columns = df.columns.str.strip().str.lower()

rev_col = get_col(df, ["revenue"])
profit_col = get_col(df, ["profit"])

for _, row in df.iterrows():
    if rev_col:
        add_triple("Company", "revenue", row[rev_col])
    if profit_col:
        add_triple("Company", "profit", row[profit_col])

# SAVE
with open("triples_structured.json", "w") as f:
    json.dump(triples, f, indent=2)

print("✅ Structured triples created successfully!")