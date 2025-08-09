import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/crypto_cleaned.csv")

# Total number of records per Network
records_per_network = df["network"].value_counts()
print(records_per_network.head())