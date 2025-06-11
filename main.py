from transaction import (
    deposit, withdraw, get_balance, transfer,
    get_transaction_history, export_transaction_history_to_csv
)
from db import initialize_database
from customer import create_customer, get_customer_id, list_customers, delete_customer
from account import create_account, list_accounts, delete_account
from dashboard import show_dashboard_summary
import os

def main():
    initialize_database()
    while True:
        print("\n--- Bank Management ---")
        print("1. Create Customer")
        print("2. View Customers")
        print("3. Create Account")
        print("4. View Accounts")
        print("5. Deposit")
        print("6. Withdraw")
        print("7. Check Balance")
        print("8. Transfer Money")
        print("9. View Transaction History")
        print("10. Delete Customer")
        print("11. Delete Account")
        print("12. Export Transaction History to CSV")
        print("13. Clear Screen")
        print("14. Show Dashboard Summary")
        print("15. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            create_customer(name, email, phone)

        elif choice == '2':
            customers = list_customers()
            if customers:
                print("\nCustomer List:")
                for cust in customers:
                    print(f"ID: {cust[0]}, Name: {cust[1]}, Email: {cust[2]}, Phone: {cust[3]}")
            else:
                print("No customers found.")

        elif choice == '3':
            email = input("Enter customer email to create account for: ")
            customer_id = get_customer_id(email)
            if not customer_id:
                print("Customer not found!")
            else:
                account_type = input("Enter account type (Savings/Current): ")
                if account_type not in ['Savings', 'Current']:
                    print("Invalid account type.")
                else:
                    create_account(customer_id, account_type)

        elif choice == '4':
            accounts = list_accounts()
            if accounts:
                print("\nAccounts List:")
                for acc in accounts:
                    print(f"Account ID: {acc[0]}, Customer ID: {acc[1]}, Type: {acc[2]}, Balance: ₹{acc[3]}")
            else:
                print("No accounts found.")

        elif choice == '5':
            acc_id = input("Enter account ID to deposit into: ")
            amount = float(input("Enter amount to deposit: "))
            deposit(acc_id, amount)

        elif choice == '6':
            acc_id = input("Enter account ID to withdraw from: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw(acc_id, amount)

        elif choice == '7':
            try:
                account_id = int(input("Enter account ID to check balance: "))
                balance = get_balance(account_id)
                if balance is not None:
                    print(f"Balance for account ID {account_id} is ₹{balance}.")
                else:
                    print("Account not found or error retrieving balance.")
            except ValueError:
                print("Invalid account ID. Please enter a number.")

        elif choice == '8':
            try:
                from_account = int(input("Enter source account ID: "))
                to_account = int(input("Enter destination account ID: "))
                amount = float(input("Enter amount to transfer: "))
                transfer(from_account, to_account, amount)
            except ValueError:
                print("Invalid input. Please enter valid numbers for account IDs and amount.")

        elif choice == '9':
            try:
                account_id = int(input("Enter account ID to view transaction history: "))
                history = get_transaction_history(account_id)
                if history:
                    print(f"\nTransaction History for Account ID {account_id}:")
                    for txn in history:
                        print(f"ID: {txn[0]}, Type: {txn[1]}, Amount: ₹{txn[2]}, Date: {txn[3]}")
                else:
                    print("No transactions found for this account.")
            except ValueError:
                print("Invalid account ID. Please enter a number.")

        elif choice == '10':
            try:
                customer_id = int(input("Enter customer ID to delete: "))
                delete_customer(customer_id)
            except ValueError:
                print("Invalid customer ID.")

        elif choice == '11':
            try:
                account_id = int(input("Enter account ID to delete: "))
                delete_account(account_id)
            except ValueError:
                print("Invalid account ID.")

        elif choice == '12':
            try:
                account_id = int(input("Enter account ID to export transactions to CSV: "))
                filename = input("Enter CSV filename (e.g., transactions.csv): ")
                export_transaction_history_to_csv(account_id, filename)
            except ValueError:
                print("Invalid account ID.")

        elif choice == '13':
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == '14':
            show_dashboard_summary()

        elif choice == '15':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
