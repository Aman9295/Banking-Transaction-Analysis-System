import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

os.makedirs("reports", exist_ok=True)
os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/transactions.csv")

df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

df["Suspicious_Reason"] = ""

df.loc[df["Amount"] >= 50000, "Suspicious_Reason"] += "High Value Transaction; "
df.loc[df["Status"] == "Failed", "Suspicious_Reason"] += "Failed Transaction; "
df.loc[
    (df["Transaction_Time"] >= "22:00") | (df["Transaction_Time"] <= "05:00"),
    "Suspicious_Reason"
] += "Unusual Night Transaction; "

suspicious_df = df[df["Suspicious_Reason"] != ""]

summary = {
    "Total Transactions": len(df),
    "Total Transaction Amount": df["Amount"].sum(),
    "Average Transaction Amount": round(df["Amount"].mean(), 2),
    "Highest Transaction Amount": df["Amount"].max(),
    "Successful Transactions": len(df[df["Status"] == "Success"]),
    "Failed Transactions": len(df[df["Status"] == "Failed"]),
    "Suspicious Transactions": len(suspicious_df)
}

print("===== Banking Transaction Analysis System =====")
for key, value in summary.items():
    print(key, ":", value)

customer_report = df.groupby(["Customer_ID", "Customer_Name"])["Amount"].agg(
    Total_Amount="sum",
    Average_Amount="mean",
    Transaction_Count="count"
).reset_index()

channel_report = df.groupby("Channel")["Amount"].agg(
    Total_Amount="sum",
    Transaction_Count="count"
).reset_index()

type_report = df.groupby("Transaction_Type")["Amount"].agg(
    Total_Amount="sum",
    Transaction_Count="count"
).reset_index()

daily_report = df.groupby("Transaction_Date")["Amount"].sum().reset_index()

suspicious_df.to_csv("reports/suspicious_transactions.csv", index=False)
df.to_csv("reports/dashboard_data.csv", index=False)

with pd.ExcelWriter("reports/summary_report.xlsx") as writer:
    pd.DataFrame([summary]).to_excel(writer, sheet_name="Summary", index=False)
    customer_report.to_excel(writer, sheet_name="Customer_Report", index=False)
    channel_report.to_excel(writer, sheet_name="Channel_Report", index=False)
    type_report.to_excel(writer, sheet_name="Type_Report", index=False)
    daily_report.to_excel(writer, sheet_name="Daily_Report", index=False)
    suspicious_df.to_excel(writer, sheet_name="Suspicious_Transactions", index=False)

plt.figure()
type_report.plot(kind="bar", x="Transaction_Type", y="Total_Amount", legend=False)
plt.title("Transaction Amount by Type")
plt.xlabel("Transaction Type")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("charts/transaction_by_type.png")

plt.figure()
channel_report.plot(kind="bar", x="Channel", y="Total_Amount", legend=False)
plt.title("Transaction Amount by Channel")
plt.xlabel("Channel")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("charts/transaction_by_channel.png")

plt.figure()
daily_report.plot(kind="line", x="Transaction_Date", y="Amount", marker="o", legend=False)
plt.title("Daily Transaction Amount")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("charts/daily_transaction_amount.png")

conn = sqlite3.connect("database/banking.db")

df.to_sql("transactions", conn, if_exists="replace", index=False)
suspicious_df.to_sql("suspicious_transactions", conn, if_exists="replace", index=False)

conn.close()

print("\nReports and charts generated successfully.")