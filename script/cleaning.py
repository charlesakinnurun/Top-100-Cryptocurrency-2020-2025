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