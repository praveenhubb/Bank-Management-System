from db import get_connection
from colorama import Fore, Style

def create_account(customer_id, account_type):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO accounts (customer_id, account_type, balance) VALUES (?, ?, ?)",
            (customer_id, account_type, 0)
        )
        conn.commit()
        print(f"Account '{account_type}' created for customer ID {customer_id}.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def list_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT account_id, customer_id, account_type, balance FROM accounts
    """)
    accounts = cursor.fetchall()
    conn.close()
    return accounts

def delete_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Delete related transactions first
        cursor.execute("DELETE FROM transactions WHERE account_id = ?", (account_id,))
        # Then delete the account
        cursor.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,))
        conn.commit()
        print(Fore.GREEN + f"✅ Account ID {account_id} and its transactions deleted successfully." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"❌ Error deleting account: {e}" + Style.RESET_ALL)
    finally:
        conn.close()
