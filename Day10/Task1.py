import pandas as pd
data = {
    "Price": ["$100", "$250", "$175", "$300"],
    "Date": ["2025-01-10", "2025-02-15", "2025-03-20", "2025-04-25"]
}
df = pd.DataFrame(data)
print("Initial Data Types:")
print(df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
print("\nUpdated Data Types:")
print(df.dtypes)
print("\nFinal DataFrame:")
print(df)
