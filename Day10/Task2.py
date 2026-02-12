import pandas as pd
data = {
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", " los angeles "]
}
df = pd.DataFrame(data)
print("Unique values before cleaning:")
print(df["Location"].unique())
df["Location"] = df["Location"].str.strip().str.title()
print("\nUnique values after cleaning:")
print(df["Location"].unique())
