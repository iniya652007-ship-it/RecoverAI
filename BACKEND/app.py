import pandas as pd
df = pd.read_csv(r"C:\Users\Iniya\OneDrive\Documents\OQVANTA\Transactions.csv")
print(df.columns)
print("OQVANTA ANALYSIS IS ABOUT TO START")

print("OQVANTA is starting to run...")
print("Intelligent Revenue Recovery Agent is running")
print("the system status detected is :ONLINE")

print("Transaction Summary")

print("TOTAL TRANSACTIONS ARE:", len(df))
print("TOTAL AMOUNT IS:", df["amount"].sum())
print("AVERAGE AMOUNT IS:", df["amount"].mean())
print("HIGHEST TRANSACTION IS:", df["amount"].max())
successful_transactions = df[df["status"] == "success"]
failed_transactions = df[df["status"] == "failed"]
print("SUCCESSFUL TRANSACTIONS ARE:", len(successful_transactions))
print("FAILED TRANSACTIONS ARE:", len(failed_transactions))

print("Amount from failed transactions:",failed_transactions["amount"].sum())


print("PAYMENT METHODS USED")
print(df["payment_method"].value_counts())

print("\n--- FAILED TRANSACTIONS ---")
print(failed_transactions)

high_value_failed_transactions = failed_transactions[failed_transactions["amount"] > 500]

print("HIGH VALUE FAILED TRANSACTIONS AMOUNT")
print(high_value_failed_transactions)

success_rate=len(successful_transactions)/len(df)*100
print("SUCCESS RATE IS :",success_rate,"%")
failure_rate = (len(failed_transactions) / len(df)) * 100
print("FAILURE RATE:", failure_rate, "%")

FAILED_TOTAL_REVENUE= failed_transactions["amount"].sum()
print("TOTAL REVENUE FROM FAILED TRANSACTIONS:", FAILED_TOTAL_REVENUE)
FAILED_TRANSACTIONS_USING_UPI = failed_transactions["payment_method"].value_counts().get("upi")
print("TRY RETRYING THE PAYMENT FOR UPI:", FAILED_TRANSACTIONS_USING_UPI)
FAILED_TRANSACTIONS_USING_CARD = failed_transactions["payment_method"].value_counts().get("card")
print("SUGGEST CHECKING THE CORRECT CARD DETAILS OR TRY SOME OTHER PAYMENT METHOD:", FAILED_TRANSACTIONS_USING_CARD)

MOST_USED_PAYMENT_METHOD = df["payment_method"].value_counts().idxmax()
print("MOST USED PAYMENT METHOD IS:", MOST_USED_PAYMENT_METHOD)

print("CUSTOMER DETAILS AS FOLLOWS...")

while True:
    print("\nCUSTOMER DETAILS AS FOLLOWS...")

    customer_id = input("Enter customer id: ")
    customer_name = input("Enter customer name: ")
    amount = float(input("Enter amount: "))
    payment_method = input("Enter payment method: ")
    status = input("Enter status: ")

    NEW_TRANSACTION = {
        "customer_id": customer_id,
        "customer_name": customer_name,
        "amount": amount,
        "payment_method": payment_method,
        "status": status
    }
    if amount<=0:
        print("Amount should be greater than 0")
    elif payment_method not in["upi","card"]:
        print("Payment method should be either upi or card")
    elif status not in ["success","failed"]:
        print("Status should be either success or failed")
    else:
        df = pd.concat([df, pd.DataFrame([NEW_TRANSACTION])], ignore_index=True)
        df.to_csv(
            r"C:\Users\Iniya\OneDrive\Documents\OQVANTA\Transactions.csv",
            index=False
        )
        print("TRANSACTION SAVED SUCCESSFULLY!")

    choice = input("Do you want to add another transaction? (yes/no): ")

    if choice.lower() == "no":
        print("\nTHANK YOU FOR USING OQVANTA!")
        break
  

