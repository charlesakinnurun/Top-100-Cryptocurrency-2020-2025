import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# 7-Day Rolling Average for Ethereum

# Filter for ETHUSDT and sort by date
eth_data = df[df["symbol"] == "ETHUSDT"].sort_values("date")

# Calculate the 7-day rolling average of the closing price
eth_data["7_day_rolling_avg"] = eth_data["close"].rolling(window=7).mean()

# Display the Result
print(eth_data[["date","close","7_day_rolling_avg"]].tail(7))