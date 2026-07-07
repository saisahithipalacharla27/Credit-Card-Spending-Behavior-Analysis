import pandas as pd

# Read cleaned Excel workbook
customers = pd.read_excel(
    "data/cleaned/cleaned_excel.xlsx",
    sheet_name="Customers"
)

transactions = pd.read_excel(
    "data/cleaned/cleaned_excel.xlsx",
    sheet_name="Transactions"
)

# Preview data
print("Customers Dataset")
print(customers.head())

print("\nTransactions Dataset")
print(transactions.head())

# Dataset information
print("\nCustomers Info")
customers.info()

print("\nTransactions Info")
transactions.info()

# Missing values
print("\nMissing Values - Customers")
print(customers.isnull().sum())

print("\nMissing Values - Transactions")
print(transactions.isnull().sum())

# Duplicate records
print("\nDuplicate Customers:", customers.duplicated().sum())
print("Duplicate Transactions:", transactions.duplicated().sum())

# Convert date column
transactions["Transaction_Date"] = pd.to_datetime(
    transactions["Transaction_Date"]
)

print("\nUpdated Data Types")
print(transactions.dtypes)

# Export cleaned CSV files
customers.to_csv(
    "data/cleaned/customers_cleaned.csv",
    index=False
)

transactions.to_csv(
    "data/cleaned/transactions_cleaned.csv",
    index=False
)

print("\nData validation completed successfully!")
print("Cleaned CSV files exported to data/cleaned/")