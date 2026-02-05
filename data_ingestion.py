import pandas as pd

print("===== DATA INGESTION STARTED =====")

# 1. Ingest STRUCTURED data (CSV)
structured_df = pd.read_csv("structured_dataset_100.csv")
print("\nStructured Data Loaded Successfully")
print(structured_df.head())

# 2. Ingest SEMI-STRUCTURED data (CSV)
semi_structured_df = pd.read_csv("semi_structured_dataset_100.csv")
print("\nSemi-Structured Data Loaded Successfully")
print(semi_structured_df.head())

# 3. Ingest UNSTRUCTURED data (CSV containing text)
unstructured_df = pd.read_csv("unstructured_dataset_100.csv")
print("\nUnstructured Data Loaded Successfully")
print(unstructured_df.head())

print("\n===== DATA INGESTION COMPLETED =====")