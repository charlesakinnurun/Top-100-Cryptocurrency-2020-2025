import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Convert date column to datetime objects
df["date"] = pd.to_datetime(df["date"])

# Filter for the year 2023
df_2023 = df[df["date"].dt.year == 2023]

# Group by symbol and find the average closing price for 2023
avg_close_2023 = df_2023.groupby("symbol")["close"].mean().sort_values(ascending=False)

# Display the Result
print("Average Closing Price in 2023")
print(avg_close_2023.head())