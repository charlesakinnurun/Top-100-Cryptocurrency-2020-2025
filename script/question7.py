import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Largest Single-Day Price Increase

# Calculate the daily price increase
df["daily_increase"] = df["close"] - df["open"]

# Find the row with the largest daily increase
max_increase_row = df.loc[df["daily_increase"].idxmax()]

# Display the result
print(max_increase_row[["symbol","date","daily_increase"]])

