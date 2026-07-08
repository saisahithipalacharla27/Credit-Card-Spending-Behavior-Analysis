<!-- # 💳 Credit Card Spending Behavior Analysis

An end-to-end **Data Analytics** project that transforms raw credit card transaction data into actionable business insights using **Excel, Python, MySQL, SQL, and Tableau**. The project demonstrates the complete analytics workflow—from data cleaning and exploration to dashboard development and business recommendations.

---

## 📌 Project Overview

Financial institutions process millions of credit card transactions every day. Analyzing these transactions helps banks understand customer spending patterns, identify profitable customer segments, monitor fraudulent activities, and make data-driven business decisions.

This project analyzes **5,000 credit card transactions** from **3,001 customers** to uncover spending behavior, customer preferences, and revenue opportunities through an interactive Tableau dashboard.

---

## 🎯 Business Problem

Banks require actionable insights from transaction data to answer critical business questions such as:

* Which customers generate the highest revenue?
* Which merchant categories contribute the most spending?
* Which card types are the most profitable?
* Which customer segments should be targeted for premium offerings?
* How do customers prefer to make payments?
* What is the current fraud rate?
* Which business strategies can improve customer retention and profitability?

---

## 🎯 Business Objectives

* Analyze customer spending behavior.
* Identify high-value customer segments.
* Evaluate card-wise and category-wise spending.
* Measure fraud occurrence.
* Develop an executive dashboard for decision-makers.
* Generate business recommendations to improve revenue and customer engagement.

---

## 🛠️ Tools & Technologies

| Category        | Technologies                     |
| --------------- | -------------------------------- |
| Data Cleaning   | Microsoft Excel, Python (Pandas) |
| Data Analysis   | Python, SQL                      |
| Database        | MySQL                            |
| Visualization   | Tableau                          |
| Programming     | Python                           |
| Version Control | Git & GitHub                     |
| IDE             | VS Code                          |

---

## 📊 Dataset Information

| Metric                    |          Value |
| ------------------------- | -------------: |
| Total Customers           |          3,001 |
| Total Transactions        |          5,000 |
| Total Spending            | ₹47.59 Million |
| Average Transaction Value |         ₹9,518 |
| Fraud Rate                |          4.86% |

### Dataset Features

* Customer ID
* Gender
* Age Group
* Income Group
* Card Type
* Merchant Category
* Transaction Amount
* Payment Mode
* Credit Limit
* Outstanding Balance
* Reward Points
* Fraud Flag

---

## ⚙️ Project Workflow

```text
Raw CSV Dataset
        │
        ▼
Excel Data Cleaning
        │
        ▼
Python Data Cleaning & EDA
        │
        ▼
MySQL Database
        │
        ▼
SQL Business Queries
        │
        ▼
Tableau Dashboard
        │
        ▼
Business Insights & Recommendations



📈 Dashboard Features
Executive KPI Cards
Monthly Spending Trend
Merchant Category Analysis
Card Type Analysis
Top Customers
Payment Mode Distribution
Gender Analysis
Age Group Analysis
Income Group Analysis
Fraud Analysis
Interactive Filters


  🖼 Dashboard Preview

![Credit Card Dashboard](https://raw.githubusercontent.com/saisahithipalacharla27/Credit-Card-Spending-Behavior-Analysis/main/images/creditcarddashboard.png)


📌 Key Performance Indicators
KPI	Value
👥 Total Customers	3,001
💳 Total Transactions	5,000
💰 Total Spending	₹47.59 Million
📊 Average Transaction	₹9,518
🛡 Fraud Rate	4.86%
💡 Key Business Insights
💳 Customers generated ₹47.59 Million in total spending, indicating strong credit card usage.
📈 Spending remained consistent throughout the year, ensuring predictable revenue.
🛍 Electronics and ✈️ Travel contributed the highest transaction value.
🥈 Silver cardholders generated the highest total spending due to their larger customer base.
💼 High-income customers contributed the largest share of revenue.
💳 Payment methods were evenly distributed across Chip, Tap, Swipe, and Online transactions.
👥 Customers aged 55+ recorded the highest spending.
🚨 Fraud represented only a small proportion of total transactions but requires continuous monitoring.
📈 Business Recommendations
Launch premium card upgrade campaigns targeting high-performing Silver cardholders.
Partner with electronics retailers and travel companies to offer cashback and EMI benefits.
Introduce VIP loyalty programs for high-value customers.
Increase digital payment adoption through contactless payment rewards.
Strengthen fraud prevention using AI-based monitoring and real-time alerts.


📂 Repository Structure
Credit-Card-Spending-Behavior-Analysis/
│
├── data/
├── database/
├── Excel/
├── images/
├── python/
├── reports/
├── tableau/
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/saisahithipalacharla27/Credit-Card-Spending-Behavior-Analysis.git
```

### Navigate to the project

```bash
cd Credit-Card-Spending-Behavior-Analysis
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Execute Python scripts

```bash
python python/data_cleaning.py
```

### Open Dashboard

Open the Tableau workbook available in the `tableau/` folder using Tableau Desktop or Tableau Public.

---

# 📚 Skills Demonstrated

* Data Cleaning
* Data Wrangling
* Exploratory Data Analysis (EDA)
* SQL Query Writing
* Database Design
* Tableau Dashboard Development
* KPI Reporting
* Business Intelligence
* Data Visualization
* Business Storytelling
* Banking Domain Analytics
* Git & GitHub Version Control

---

# 🔮 Future Enhancements

* Build a real-time dashboard using live transaction data.
* Develop a machine learning model for fraud prediction.
* Create a Streamlit web application for interactive analytics.
* Automate monthly business reporting.
* Perform customer segmentation using clustering techniques.

---

# 📄 Project Report

A detailed Business Intelligence Report explaining the methodology, dashboard interpretation, business insights, and recommendations is available in the **reports/** folder.

---

# 👩‍💻 Author

**Sai Sahithi Palacharla**

Aspiring Data Analyst

🔗 GitHub: https://github.com/saisahithipalacharla27
💼 LinkedIn: https://www.linkedin.com/in/sahithipalacharla/ -->

# 💳 Credit Card Spending Behavior Analysis Dashboard

![Python](https://img.shields.io/badge/Python-Data%20Analysis-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Database%20Analysis-orange)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Project Overview

This project analyzes **3000+ credit card transactions** to understand customer spending behavior, transaction patterns, fraud activities, and revenue drivers across different cities, merchant categories, payment methods, and card segments.

The objective was to transform raw transaction data into actionable business insights that help banks improve:

- Customer engagement strategies
- Card usage optimization
- Fraud monitoring
- Marketing campaigns
- Revenue growth opportunities

---

## 🎯 Business Questions

The analysis focuses on answering key business questions:

- Which cities contribute the highest transaction value?
- Which merchant categories generate maximum spending?
- How do customers prefer to make payments?
- Which card types generate higher revenue?
- What patterns exist in fraudulent transactions?
- Who are the highest-value customers?

---

## 🛠️ Tools Used

- Python
- Pandas
- NumPy
- SQL
- Matplotlib
- Seaborn
- Power BI
- Excel
- Data Cleaning & Exploratory Data Analysis

---

## 📊 Data Analysis Workflow

The project follows an end-to-end analytics workflow:

### 1. Data Cleaning

- Handled missing values
- Removed duplicate transactions
- Standardized categorical fields
- Converted date columns into analysis-ready formats

### 2. Exploratory Data Analysis

Performed analysis on:

- Customer spending patterns
- Transaction trends
- City-wise contribution
- Merchant category performance
- Payment preferences
- Fraud detection patterns

### 3. Dashboard Development

Built an interactive dashboard to provide business users with quick insights.

---

## 📈 Key Metrics

The dashboard tracks important business KPIs:

- 💰 Total Spending
- 👥 Total Customers
- 💳 Total Transactions
- 📊 Average Transaction Value
- 🚨 Fraud Transaction Rate
- 🏙️ Top Performing Cities
- 🛒 Highest Revenue Categories

---

## 📊 Dashboard Features

- Executive Summary Dashboard
- Monthly Spending Trend Analysis
- City-wise Spending Analysis
- Merchant Category Performance
- Card Type Analysis
- Payment Mode Analysis
- Fraud Detection Dashboard
- Customer Segmentation
- Interactive Filters

---

## 🖼️ Dashboard Preview

![Credit Card Dashboard](https://raw.githubusercontent.com/saisahithipalacharla27/Credit-Card-Spending-Behavior-Analysis/main/images/creditcarddashboard.png)

---

## 💡 Key Business Insights

- 🏙️ Top-performing cities contribute significantly to overall transaction revenue, indicating strong customer activity in these markets.

- 💳 Premium card categories show higher spending patterns, creating opportunities for targeted upgrade campaigns.

- 🛒 Grocery, shopping, and lifestyle categories represent major spending drivers.

- 📱 Digital payment methods demonstrate strong adoption among customers.

- 🚨 Fraud transactions represent a small percentage of total activity but require continuous monitoring.

- 👥 High-value customers contribute a significant portion of total spending and can be targeted through loyalty programs.

---

## 🚀 Business Recommendations

Based on the analysis:

- Launch premium card promotions in high-spending cities.
- Provide cashback and rewards for frequently used merchant categories.
- Develop personalized offers based on customer spending behavior.
- Strengthen fraud monitoring for suspicious transaction patterns.
- Create loyalty programs for high-value customers.

---

## 📂 Repository Structure

```text
Credit-Card-Spending-Analysis/

│
├── data/
│   └── credit_card_transactions.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── sql/
│   └── analysis_queries.sql
│
├── dashboard/
│   └── Credit_Card_Dashboard.pbix
│
├── images/
│   └── dashboard.png
│
├── report/
│   └── Credit_Card_Analysis_Report.pdf
│
└── README.md