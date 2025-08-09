import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Convert the date column to datatime objects
df["date"] = pd.to_datetime(df["date"])

# Bitcoin Closing Percentage Change

# Filter for BTCUSDT and sort by date
btc_data = df[df["symbol"] == "BTCUSDT"].sort_values("date")

# Get the first and last closing price
first_close = btc_data["close"].iloc[0]
last_close = btc_data["close"].iloc[-1]

# Calculate percentage change
price_change = ((last_close - first_close) / first_close) * 100

# Display the result 
print(f"Percentage change in BTCUSDT closing Price: {price_change:.2f}%")