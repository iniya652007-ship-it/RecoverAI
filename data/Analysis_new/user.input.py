import pandas as pd

transactions = []

while True:
    customer_id = input("Enter customer id: ")
    customer_name = input("Enter customer name: ")
    amount = float(input("Enter amount: "))
    payment_method = input("Enter payment method: ")

    transaction = {
        "customer_id": customer_id,
        "customer_name": customer_name,
        "amount": amount,
        "payment_method": payment_method
    }

    transactions.append(transaction)

    choice = input("Do you want to add another transaction? (yes/no): ")

    if choice.lower() == "no":
        break

df = pd.DataFrame(transactions)

print(df)

df.to_csv("Transactions.csv", index=False)