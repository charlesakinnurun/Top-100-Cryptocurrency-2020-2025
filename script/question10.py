import pandas as pd

# Load the cleaned dataframe
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Convert the date column to datetime objects
df["date"] = pd.to_datetime(df["date"])

# Average January High Price
# Filter for the month of January across all years
january_data = df[df["date"].dt.month == 1]

# Group by symbol and find the average high price for january
avg_high_jan = january_data.groupby("symbol")["high"].mean().sort_values(ascending=False)

# Display the Result
print("Average January high price")
print(avg_high_jan.head())