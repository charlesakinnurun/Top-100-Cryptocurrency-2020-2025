import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Convert the date column to datatime objects
df["date"] = pd.to_datetime(df["date"])

# Sort the DataFrame by date and find the max
max_close_prices = df.loc[df.groupby("symbol")["close"].idxmax()][["symbol","date","close"]]
print(max_close_prices.sort_values(by= "close",ascending=False).head())