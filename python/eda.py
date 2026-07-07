import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ----------------------------------------
# Create Images Folder
# ----------------------------------------
os.makedirs("images", exist_ok=True)

# ----------------------------------------
# Read Cleaned Data
# ----------------------------------------
customers = pd.read_csv("data/cleaned/customers_cleaned.csv")
transactions = pd.read_csv("data/cleaned/transactions_cleaned.csv")

# ----------------------------------------
# Convert Date
# ----------------------------------------
transactions["Transaction_Date"] = pd.to_datetime(
    transactions["Transaction_Date"]
)

# ----------------------------------------
# Merge Datasets
# ----------------------------------------
df = pd.merge(
    transactions,
    customers,
    on="Customer_ID",
    how="left"
)

print("="*60)
print("Merged Dataset")
print("="*60)

print(df.head())

# ----------------------------------------
# Basic Dataset Information
# ----------------------------------------
print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nSummary Statistics")
print(df.describe())

# ----------------------------------------
# BUSINESS QUESTION 1
# Which city spends the most?
# ----------------------------------------

city_spending = (
    df.groupby("City")["Amount"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTop Spending Cities")
print(city_spending)

# ----------------------------------------
# BUSINESS QUESTION 2
# Highest Card Type Spending
# ----------------------------------------

card_spending = (
    df.groupby("Card_Type")["Amount"]
      .sum()
      .sort_values(ascending=False)
)

print("\nCard Type Spending")
print(card_spending)

# ----------------------------------------
# BUSINESS QUESTION 3
# Average Transaction Amount
# ----------------------------------------

average_transaction = df["Amount"].mean()

print("\nAverage Transaction Amount")
print(round(average_transaction,2))

# ----------------------------------------
# BUSINESS QUESTION 4
# Top 10 Merchants
# ----------------------------------------

top_merchants = (
    df.groupby("Merchant_Name")["Amount"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop Merchants")
print(top_merchants)

# ----------------------------------------
# BUSINESS QUESTION 5
# Monthly Spending
# ----------------------------------------

df["Month"] = df["Transaction_Date"].dt.month_name()

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

df["Month"] = pd.Categorical(
    df["Month"],
    categories=month_order,
    ordered=True
)

monthly_spending = (
    df.groupby("Month")["Amount"]
      .sum()
)

print("\nMonthly Spending")
print(monthly_spending)

# ----------------------------------------
# BUSINESS QUESTION 6
# Highest Income Group
# ----------------------------------------

df["Income_Group"] = pd.cut(
    df["Annual_Income"],
    bins=[0,500000,1000000,1500000,10000000],
    labels=[
        "Low",
        "Middle",
        "Upper Middle",
        "High"
    ]
)

income_spending = (
    df.groupby("Income_Group")["Amount"]
      .sum()
      .sort_values(ascending=False)
)

print("\nIncome Group Spending")
print(income_spending)

# ===========================================================
# VISUALIZATIONS
# ===========================================================

sns.set_style("whitegrid")

# ----------------------------------------
# 1 Card Type Spending
# ----------------------------------------

plt.figure(figsize=(8,5))

card_spending.plot(kind="bar", color="steelblue")

plt.title("Total Spending by Card Type")

plt.xlabel("Card Type")

plt.ylabel("Amount")

plt.tight_layout()

plt.savefig("images/card_type_spending.png")

plt.show()

# ----------------------------------------
# 2 Payment Mode Pie Chart
# ----------------------------------------

payment = df["Payment_Mode"].value_counts()

plt.figure(figsize=(7,7))

payment.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.ylabel("")

plt.title("Payment Mode Distribution")

plt.tight_layout()

plt.savefig("images/payment_mode_distribution.png")

plt.show()

# ----------------------------------------
# 3 Histogram
# ----------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df["Amount"],
    bins=30,
    edgecolor="black"
)

plt.title("Distribution of Transaction Amount")

plt.xlabel("Transaction Amount")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("images/transaction_histogram.png")

plt.show()

# ----------------------------------------
# 4 Box Plot
# ----------------------------------------

plt.figure(figsize=(6,5))

sns.boxplot(
    y=df["Amount"],
    color="orange"
)

plt.title("Transaction Amount Box Plot")

plt.tight_layout()

plt.savefig("images/transaction_boxplot.png")

plt.show()

# ----------------------------------------
# 5 Heatmap
# ----------------------------------------

plt.figure(figsize=(8,6))

corr = df.select_dtypes(include="number").corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/correlation_heatmap.png")

plt.show()

# ----------------------------------------
# 6 Monthly Spending Trend
# ----------------------------------------

plt.figure(figsize=(10,5))

monthly_spending.plot(
    marker="o"
)

plt.title("Monthly Spending Trend")

plt.xlabel("Month")

plt.ylabel("Total Spending")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/monthly_spending_trend.png")

plt.show()

# ----------------------------------------
# 7 Top 10 Merchants
# ----------------------------------------

plt.figure(figsize=(10,5))

top_merchants.plot(kind="bar")

plt.title("Top 10 Merchants by Spending")

plt.xlabel("Merchant")

plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/top_merchants.png")

plt.show()

print("\n" + "="*60)
print("EDA Completed Successfully")
print("Charts saved inside images/ folder")
print("="*60)