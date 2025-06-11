from db import get_connection
import datetime
import csv

def deposit(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, account_id))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO transactions (account_id, transaction_type, amount, timestamp) VALUES (?, ?, ?, ?)",
            (account_id, 'Deposit', amount, date)
        )
        conn.commit()
        print(f"Deposited ₹{amount} to account {account_id}.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def withdraw(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        balance = cursor.fetchone()
        if not balance:
            print("Account not found.")
            return False
        if balance[0] < amount:
            print("Insufficient balance.")
            return False
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_id))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO transactions (account_id, transaction_type, amount, timestamp) VALUES (?, ?, ?, ?)",
            (account_id, 'Withdraw', amount, date)
        )
        conn.commit()
        print(f"Withdrew ₹{amount} from account {account_id}.")
        return True
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        conn.close()

def get_balance(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        conn.close()

def transfer(from_account_id, to_account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_account_id,))
        from_balance = cursor.fetchone()
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (to_account_id,))
        to_balance = cursor.fetchone()

        if not from_balance:
            print(f"Source account {from_account_id} not found.")
            return
        if not to_balance:
            print(f"Destination account {to_account_id} not found.")
            return
        if from_balance[0] < amount:
            print("Insufficient balance in source account.")
            return

        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_account_id))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_account_id))

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO transactions (account_id, transaction_type, amount, timestamp) VALUES (?, ?, ?, ?)",
            (from_account_id, 'Transfer', amount, date)
        )
        cursor.execute(
            "INSERT INTO transactions (account_id, transaction_type, amount, timestamp) VALUES (?, ?, ?, ?)",
            (to_account_id, 'Transfer', amount, date)
        )

        conn.commit()
        print(f"Transferred ₹{amount} from account {from_account_id} to account {to_account_id}.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def get_transaction_history(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT transaction_id, transaction_type, amount, timestamp
            FROM transactions
            WHERE account_id = ?
            ORDER BY timestamp DESC
        """, (account_id,))
        transactions = cursor.fetchall()
        return transactions
    except Exception as e:
        print("Error:", e)
        return []
    finally:
        conn.close()

# ✅ New: Export transaction history to CSV
def export_transaction_history_to_csv(account_id, filename):
    transactions = get_transaction_history(account_id)
    if not transactions:
        print("No transactions to export.")
        return

    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Transaction ID', 'Type', 'Amount', 'Timestamp'])
            writer.writerows(transactions)
        print(f"Transaction history exported successfully to '{filename}'.")
    except Exception as e:
        print("Error exporting to CSV:", e)
