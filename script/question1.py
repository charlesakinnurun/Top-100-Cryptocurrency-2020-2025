import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Convert the date column to datetime objecta
df["date"] = pd.to_datetime(df["date"])

# Group by symbol and find the average closing price
avg_close_price = df.groupby("symbol")["close"].mean().sort_values(ascending=False)

# Display the result
print("Highest Average Closing price")
print(avg_close_price.head(1))