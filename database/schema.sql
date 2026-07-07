-- CREATE DATABASE CreditCardAnalysis; -- commented out to avoid parser error

-- USE CreditCardAnalysis;

CREATE TABLE customers (
    Customer_ID VARCHAR(20) PRIMARY KEY,
    Customer_Name VARCHAR(100) NOT NULL,
    Gender VARCHAR(20),
    Age INT,
    City VARCHAR(100),
    State VARCHAR(100),
    Occupation VARCHAR(100),
    Annual_Income DECIMAL(12,2),
    Credit_Limit DECIMAL(12,2),
    Card_Type VARCHAR(50),
    Join_Date DATE
);

CREATE TABLE transactions (
    Transaction_ID VARCHAR(20) PRIMARY KEY,
    Customer_ID VARCHAR(20) NOT NULL,
    Transaction_Date DATE,
    Merchant_Name VARCHAR(100),
    Merchant_Category VARCHAR(100),
    Amount DECIMAL(12,2),
    Payment_Mode VARCHAR(50),
    Reward_Points INT,
    Transaction_Status VARCHAR(20),
    Fraud_Flag VARCHAR(10),
    Outstanding_Balance DECIMAL(12,2),
    CONSTRAINT fk_customer
        FOREIGN KEY (Customer_ID)
        REFERENCES customers(Customer_ID)
);