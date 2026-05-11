import sqlite3
import pandas as pd
import os

os.makedirs("database", exist_ok=True)

df = pd.read_csv("data/transactions.csv")

conn = sqlite3.connect("database/banking.db")

df.to_sql("transactions", conn, if_exists="replace", index=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS suspicious_transactions (
    Transaction_ID TEXT,
    Customer_ID TEXT,
    Customer_Name TEXT,
    Amount REAL,
    Transaction_Date TEXT,
    Transaction_Time TEXT,
    Location TEXT,
    Channel TEXT,
    Reason TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully and transaction data inserted.")