import pandas as pd

print("===== DATA NORMALIZATION STARTED =====")

# -------------------------------
# LOAD INGESTED DATA
# -------------------------------
structured_df = pd.read_csv("structured_dataset_100.csv")
semi_structured_df = pd.read_csv("semi_structured_dataset_100.csv")
unstructured_df = pd.read_csv("unstructured_dataset_100.csv")

# =================================================
# 1. NORMALIZE STRUCTURED DATA
# =================================================
print("\nNormalizing Structured Data...")

# Normalize column names
structured_df.columns = (
    structured_df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

# Remove duplicates
structured_df.drop_duplicates(inplace=True)

# Handle missing values
structured_df.fillna("Unknown", inplace=True)

# Standardize text columns
for col in structured_df.select_dtypes(include="object"):
    structured_df[col] = structured_df[col].str.title()

print("Structured Data Normalized")
print(structured_df.head())


# =================================================
# 2. NORMALIZE SEMI-STRUCTURED DATA
# =================================================
print("\nNormalizing Semi-Structured Data...")

semi_structured_df.columns = (
    semi_structured_df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

semi_structured_df.drop_duplicates(inplace=True)
semi_structured_df.fillna("Unknown", inplace=True)

for col in semi_structured_df.select_dtypes(include="object"):
    semi_structured_df[col] = semi_structured_df[col].str.title()

print("Semi-Structured Data Normalized")
print(semi_structured_df.head())


# =================================================
# 3. NORMALIZE UNSTRUCTURED DATA
# =================================================
print("\nNormalizing Unstructured Data...")

for col in unstructured_df.columns:
    unstructured_df[col] = (
        unstructured_df[col]
        .astype(str)
        .str.lower()
        .str.replace("\n", " ")
        .str.strip()
    )

print("Unstructured Data Normalized")
print(unstructured_df.head())


# =================================================
# SAVE NORMALIZED OUTPUT AS JSON
# =================================================
structured_df.to_json(
    "structured_normalized.json",
    orient="records",
    indent=4
)

semi_structured_df.to_json(
    "semi_structured_normalized.json",
    orient="records",
    indent=4
)

unstructured_df.to_json(
    "unstructured_normalized.json",
    orient="records",
    indent=4
)

print("\n===== DATA NORMALIZATION COMPLETED =====")
print("JSON files generated successfully")