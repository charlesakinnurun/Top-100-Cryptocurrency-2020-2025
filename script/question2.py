import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Calculate the trading range
df["trading_range"] = df["high"] - df["low"]

# Group by symbol and find the average trading range
avg_trading_range = df.groupby("symbol")["trading_range"].mean().sort_values(ascending=False)

# Display the result
print("Average Daily Trading Range")
print(avg_trading_range.head())