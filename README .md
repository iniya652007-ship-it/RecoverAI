# OQVANTA

## Payment Recovery System

OQVANTA is a payment recovery project that analyzes failed transactions and helps identify which payments need attention.

The system takes transaction data, separates successful and failed payments, calculates the amount of revenue at risk, checks which payment methods are failing, and highlights high-value failed transactions.

It also gives simple recovery suggestions based on the payment method. The results are shown through a Streamlit dashboard so that the transaction data is easier to understand.

## Problem Statement

Failed payments can result in lost revenue. However, not every failed transaction has the same importance.

OQVANTA focuses on finding important failed transactions, understanding basic patterns in the data, and suggesting what could be tried next.

## Features
- Add and validate transactions
- Store transaction data in CSV
- Identify failed payments
- Calculate revenue at risk
- Find high-value failed payments
- Analyze failed payment methods
- Suggest recovery actions
- Display results using a dashboard

## How It Functions?
1. Transaction details are entered into the system.
2. The transaction data is validated.
3. Data is stored in a CSV file.
4. Successful and failed transactions are separated.
5. Failed transaction amounts are analyzed.
6. High-value failed payments are identified.
7. Payment methods are checked for failure patterns.
8. Recovery suggestions are displayed on the dashboard.

## Technology used:
- Python
- Pandas
- Streamlit
- CSV
- Git
- GitHub

## Project Structure

OQVANTA/
│
├── BACKEND/
│   ├── app.py
│   └── dashboard.py
│
├── data/
│   └── Transactions.csv
│
└── README.md

## Dashboard

The dashboard shows:
- Total transactions
- Successful payments
- Failed payments
- Revenue at risk
- Failed payment methods
- High-value failed transactions
- Recovery suggestions

## Future Improvements
- Add detailed failure reasons
- Add transaction filters
- Improve recovery suggestions
- Add transaction history and trends
- Connect with a real payment API

## Learning

This project helped me practice:
- Python
- Pandas
- CSV handling
- Data validation
- Basic data analysis
- Streamlit
- Git and GitHub

## Author

built as a learning project to understand how transaction data can be analyzed and used to identify payment recovery opportunities for failed trnasactiond and improverise it further!.
 
