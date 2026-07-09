 --USE CreditCardAnalysis; -- commented out to avoid parser error

-- =====================================================
-- 1. View Customers
-- =====================================================

SELECT * FROM customers;

-- =====================================================
-- 2. View Transactions
-- =====================================================

SELECT * FROM transactions;

-- =====================================================
-- 3. Total Number of Customers
-- =====================================================

SELECT COUNT(*) AS Total_Customers
FROM customers;

-- =====================================================
-- 4. Total Number of Transactions
-- =====================================================

SELECT COUNT(*) AS Total_Transactions
FROM transactions;

-- =====================================================
-- 5. Total Spending
-- =====================================================

SELECT SUM(Amount) AS Total_Spending
FROM transactions;

-- =====================================================
-- 6. Average Transaction Amount
-- =====================================================

SELECT AVG(Amount) AS Average_Transaction
FROM transactions;

-- =====================================================
-- 7. Highest Spending Customer
-- =====================================================

SELECT
    Customer_ID,
    SUM(Amount) AS Total_Spending
FROM transactions
GROUP BY Customer_ID
ORDER BY Total_Spending DESC
LIMIT 1;

-- =====================================================
-- 8. Top 10 Customers
-- =====================================================

SELECT
    Customer_ID,
    SUM(Amount) AS Total_Spending
FROM transactions
GROUP BY Customer_ID
ORDER BY Total_Spending DESC
LIMIT 10;

-- =====================================================
-- 9. Top Spending Cities
-- =====================================================

SELECT
    c.City,
    SUM(t.Amount) AS Total_Spending
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.City
ORDER BY Total_Spending DESC;

-- =====================================================
-- 10. Top Merchant Categories
-- =====================================================

SELECT
    Merchant_Category,
    SUM(Amount) AS Total_Spending
FROM transactions
GROUP BY Merchant_Category
ORDER BY Total_Spending DESC;

-- =====================================================
-- 11. Top Merchants
-- =====================================================

SELECT
    Merchant_Name,
    SUM(Amount) AS Total_Spending
FROM transactions
GROUP BY Merchant_Name
ORDER BY Total_Spending DESC
LIMIT 10;

-- ====================================================
-- 12. Monthly Spending
-- ====================================================

SELECT
    MONTHNAME(Transaction_Date) AS Month,
    SUM(Amount) AS Total_Spending
FROM transactions
GROUP BY MONTH(Transaction_Date), MONTHNAME(Transaction_Date)
ORDER BY MONTH(Transaction_Date);

-- =====================================================
-- 13. Card Type Usage
-- =====================================================

SELECT
    Card_Type,
    COUNT(*) AS Customer_Count
FROM customers
GROUP BY Card_Type
ORDER BY Customer_Count DESC;

-- =====================================================
-- 14. Card Type Spending
-- =====================================================

SELECT
    c.Card_Type,
    SUM(t.Amount) AS Total_Spending
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.Card_Type
ORDER BY Total_Spending DESC;

-- =====================================================
-- 15. Payment Mode Usage
-- =====================================================

SELECT
    Payment_Mode,
    COUNT(*) AS Transactions
FROM transactions
GROUP BY Payment_Mode
ORDER BY Transactions DESC;

-- =====================================================
-- 16. Payment Mode Spending
-- =====================================================

SELECT
    Payment_Mode,
    SUM(Amount) AS Total_Spending
FROM transactions
GROUP BY Payment_Mode
ORDER BY Total_Spending DESC;

-- =====================================================
-- 17. Average Spending by City
-- =====================================================

SELECT
    c.City,
    AVG(t.Amount) AS Average_Spending
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.City
ORDER BY Average_Spending DESC;

-- =====================================================
-- 18. Transactions per Customer
-- =====================================================

SELECT
    Customer_ID,
    COUNT(*) AS Total_Transactions
FROM transactions
GROUP BY Customer_ID
ORDER BY Total_Transactions DESC;

-- =====================================================
-- 19. Highest Single Transaction
-- =====================================================

SELECT *
FROM transactions
ORDER BY Amount DESC
LIMIT 1;

-- =====================================================
-- 20. Lowest Transaction
-- =====================================================

SELECT *
FROM transactions
ORDER BY Amount ASC
LIMIT 1;

-- =====================================================
-- 21. Spending by Gender
-- =====================================================

SELECT
    c.Gender,
    SUM(t.Amount) AS Total_Spending
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.Gender;

-- =====================================================
-- 22. Spending by Occupation
-- =====================================================

SELECT
    c.Occupation,
    SUM(t.Amount) AS Total_Spending
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.Occupation
ORDER BY Total_Spending DESC;

-- =====================================================
-- 23. Customers with More Than 5 Transactions
-- =====================================================

SELECT
    Customer_ID,
    COUNT(*) AS Total_Transactions
FROM transactions
GROUP BY Customer_ID
HAVING COUNT(*) > 5
ORDER BY Total_Transactions DESC;

-- =====================================================
-- 24. Fraud Count (Example Rule)
-- Transactions Above ₹50,000
-- =====================================================

SELECT
    COUNT(*) AS Suspected_Fraud_Transactions
FROM transactions
WHERE Amount > 50000;

-- =====================================================
-- 25. High Value Transactions
-- =====================================================

SELECT *
FROM transactions
WHERE Amount > 50000
ORDER BY Amount DESC;