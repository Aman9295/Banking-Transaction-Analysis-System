# Banking Transaction Analysis System

## Project Overview
This project analyses banking transaction data using Python, SQL, Pandas, and data visualization techniques. The system identifies suspicious transactions, generates reports, and creates dashboard-ready datasets for banking analytics and audit monitoring.

---

## Features
- Transaction data analysis
- Suspicious transaction detection
- SQL database storage using SQLite
- Customer-wise transaction summary
- Channel-wise and transaction-type reporting
- Automated Excel and CSV report generation
- Chart generation using Matplotlib
- Dashboard-ready dataset for Tableau/Power BI

---

## Technologies Used
- Python
- Pandas
- SQLite
- SQL
- Excel
- Matplotlib
- Tableau / Power BI

---

## Suspicious Transaction Rules
Transactions are flagged as suspicious if:
- Amount >= 50,000
- Transaction status is Failed
- Transaction time is between 10 PM and 5 AM

---

## Reports Generated
- suspicious_transactions.csv
- summary_report.xlsx
- dashboard_data.csv

---

## Charts Generated
- Transaction Amount by Type
- Transaction Amount by Channel
- Daily Transaction Trend

---

## Project Structure

Banking_Transaction_Analysis/
│
├── data/
├── database/
├── reports/
├── charts/
├── banking_analysis.py
├── database_setup.py
├── sql_queries.sql
├── requirements.txt
└── README.md

---

## Project Use Case
This project can be used for:
- Banking analytics
- Audit monitoring
- Fraud pattern identification
- Transaction reporting
- Business intelligence dashboards

---

## Developed By
Aman Pandey