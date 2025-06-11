import streamlit as st
from customer import create_customer, list_customers, get_customer_id
from account import create_account, list_accounts
from transaction import (
    deposit, withdraw, transfer,
    get_transaction_history, export_transaction_history_to_csv
)
import pandas as pd

st.set_page_config(page_title="Bank Management System", layout="centered")
st.title("\U0001F4B0 Bank Management System")

menu = [
    "Create Customer",
    "View Customers",
    "Create Account",
    "View Accounts",
    "Deposit",
    "Withdraw",
    "Transfer",
    "Transaction History",
    "Export Transactions to CSV"
]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Customer":
    st.header("Create Customer")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    if st.button("Create"):
        create_customer(name, email, phone)
        st.success("Customer created successfully")

elif choice == "View Customers":
    st.header("Customer List")
    customers = list_customers()
    if customers:
        st.table(customers)
    else:
        st.info("No customers found.")

elif choice == "Create Account":
    st.header("Create Account")
    email = st.text_input("Customer Email")
    acc_type = st.selectbox("Account Type", ["Savings", "Current"])
    if st.button("Create Account"):
        cust_id = get_customer_id(email)
        if cust_id:
            create_account(cust_id, acc_type)
            st.success("Account created successfully")
        else:
            st.error("Customer not found")

elif choice == "View Accounts":
    st.header("Accounts List")
    accounts = list_accounts()
    if accounts:
        st.table(accounts)
    else:
        st.info("No accounts found.")

elif choice == "Deposit":
    st.header("Deposit")
    acc_id = st.text_input("Account ID")
    amount = st.number_input("Amount", min_value=0.0)
    if st.button("Deposit"):
        deposit(acc_id, amount)
        st.success(f"Deposited ₹{amount} into Account {acc_id}")

elif choice == "Withdraw":
    st.header("Withdraw")
    acc_id = st.text_input("Account ID")
    amount = st.number_input("Amount", min_value=0.0)
    if st.button("Withdraw"):
        withdraw(acc_id, amount)
        st.success(f"Withdrew ₹{amount} from Account {acc_id}")

elif choice == "Transfer":
    st.header("Transfer Money")
    from_acc = st.text_input("From Account ID")
    to_acc = st.text_input("To Account ID")
    amount = st.number_input("Amount", min_value=0.0)
    if st.button("Transfer"):
        transfer(from_acc, to_acc, amount)
        st.success(f"Transferred ₹{amount} from {from_acc} to {to_acc}")

elif choice == "Transaction History":
    st.header("Transaction History")
    acc_id = st.text_input("Account ID")
    if st.button("Show History"):
        history = get_transaction_history(acc_id)
        if history:
            st.table(history)
        else:
            st.warning("No transactions found.")

elif choice == "Export Transactions to CSV":
    st.header("Export Transactions to CSV")
    acc_id = st.text_input("Account ID")
    filename = st.text_input("CSV File Name", value="transactions.csv")
    if st.button("Export"):
        if acc_id and filename:
            export_transaction_history_to_csv(acc_id, filename)
            st.success(f"Transactions exported to {filename}")
        else:
            st.warning("Please provide both Account ID and file name.")
