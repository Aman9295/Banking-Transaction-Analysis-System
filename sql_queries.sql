-- View all transactions
SELECT * FROM transactions;

-- Total transaction amount
SELECT SUM(Amount) AS Total_Amount
FROM transactions;

-- Count transactions by channel
SELECT Channel, COUNT(*) AS Transaction_Count
FROM transactions
GROUP BY Channel;

-- High value transactions
SELECT *
FROM transactions
WHERE Amount >= 50000;

-- Failed transactions
SELECT *
FROM transactions
WHERE Status = 'Failed';

-- Customer-wise transaction summary
SELECT 
    Customer_ID,
    Customer_Name,
    COUNT(*) AS Transaction_Count,
    SUM(Amount) AS Total_Amount,
    AVG(Amount) AS Average_Amount
FROM transactions
GROUP BY Customer_ID, Customer_Name
ORDER BY Total_Amount DESC;

-- Location-wise amount
SELECT Location, SUM(Amount) AS Total_Amount
FROM transactions
GROUP BY Location
ORDER BY Total_Amount DESC;

-- Suspicious transactions
SELECT *
FROM suspicious_transactions;