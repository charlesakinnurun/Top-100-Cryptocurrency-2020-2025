## Introduction
The crypto.csv file is a dataset containing cryptocurrency price information. It includes data for various cryptocurrencies across different networks.
### Data Cleaning
```python
import pandas as pd

# Load the DataFrame
df = pd.read_csv("datasets/crypto.csv")

# Print some useful information
print(df.head())
print(df.info())

# Convert the "date" column to datetime objects
df["date"] = pd.to_datetime(df["date"])

# Check for and remove duplicate rows
initial_rows = len(df)
df = df.drop_duplicates()
final_rows = len(df)

# Check the number of rows removed to confirm if there were any duplicates
rows_removed = initial_rows - final_rows
print(f"Number of duplicates rows removed: {rows_removed}")

# Print the info of the cleaned dataframe to verify the changes
print(df.info())

# Save the cleaned data
df.to_csv("datasets/crypto_cleaned.csv")
print("Saved Successfully")
```
### Analysis
Here are 10 analytical questions that you can solve using pandas:
1. Which cryptocurrency had the highest average closing price over the entire period?
2. What was the average daily trading range (high minus low) for each cryptocurrency?
3. For each cryptocurrency, what was the highest closing price and the date it occurred?
4. How many unique cryptocurrencies are there in the dataset?
5. What was the total number of records for each network?
6. What was the percentage change in the closing price for Bitcoin (BTCUSDT) from its first date to its last date?
7. Which cryptocurrency had the largest single-day price increase (based on the difference between close and open)?
8. What was the average daily closing price for each cryptocurrency in the year 2023?
9. Calculate the 7-day rolling average of the closing price for Ethereum (ETHUSDT).
10. What was the average high price for each cryptocurrency for the month of January across all years?
#### Which cryptocurrency had the highest average closing price over the entire period?
```python
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
```
#### What was the average daily trading range (high minus low) for each cryptocurrency?
```python
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
```
#### For each cryptocurrency, what was the highest closing price and the date it occurred?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Convert the date column to datatime objects
df["date"] = pd.to_datetime(df["date"])

# Sort the DataFrame by date and find the max
max_close_prices = df.loc[df.groupby("symbol")["close"].idxmax()][["symbol","date","close"]]
print(max_close_prices.sort_values(by= "close",ascending=False).head())
```
#### How many unique cryptocurrencies are there in the dataset?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Number of Unique Cryptocurrencies
num_unique_cryptos = df["symbol"].nunique()

# Display the result 
print(f"Number of unique cryptocurrencies: {num_unique_cryptos}")
```
#### What was the total number of records for each network?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Total number of records per Network
records_per_network = df["network"].value_counts()
print(records_per_network.head())
```
#### What was the percentage change in the closing price for Bitcoin (BTCUSDT) from its first date to its last date?
```python
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
```
#### Which cryptocurrency had the largest single-day price increase (based on the difference between close and open)?
```python
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
```
#### What was the average daily closing price for each cryptocurrency in the year 2023?
```python
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
```
#### Calculate the 7-day rolling average of the closing price for Ethereum (ETHUSDT).
```python
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
```
#### What was the average high price for each cryptocurrency for the month of January across all years?
```python
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
```
