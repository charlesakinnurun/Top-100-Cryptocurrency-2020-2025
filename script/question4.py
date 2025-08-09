import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Number of Unique Cryptocurrencies
num_unique_cryptos = df["symbol"].nunique()

# Display the result 
print(f"Number of unique cryptocurrencies: {num_unique_cryptos}")