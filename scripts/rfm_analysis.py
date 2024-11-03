import pandas as pd

# Use the absolute path to the dataset file
file_path = "C:/Users/alina/OneDrive/Desktop/University/Bachelor/RFM_Analysis_Project/data/online_retail_ii.csv"

# Load the dataset into a DataFrame
try:
    data = pd.read_csv(file_path, encoding="ISO-8859-1")
    print("Data loaded successfully!")
    print(data.head())
except FileNotFoundError:
    print("The file was not found. Check the file path and try again.")

# Display basic information about the dataset
print(data.info())      # Shows column names, data types, and non-null counts
print(data.describe())  # Provides summary statistics for numerical columns
print(data.head())      # Shows the first few rows to inspect column contents

# Check for missing values in each column
print(data.isnull().sum())

# Check total number of rows and columns in the dataset
total_rows, total_columns = data.shape
print(f"Total rows: {total_rows}")
print(f"Total columns: {total_columns}")

# Calculate percentage of rows with missing Customer IDs
missing_customer_id_count = 107927  # as per your previous output
percentage_missing = (missing_customer_id_count / total_rows) * 100
print(f"Percentage of rows with missing Customer IDs: {percentage_missing:.2f}%")

# Drop rows where Customer ID is missing
data = data.dropna(subset=['Customer ID'])

# Check for missing values in each column
print(data.isnull().sum())