from db import get_connection

def show_dashboard_summary():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Total Customers
        cursor.execute("SELECT COUNT(*) FROM customers")
        total_customers = cursor.fetchone()[0]

        # Total Accounts
        cursor.execute("SELECT COUNT(*) FROM accounts")
        total_accounts = cursor.fetchone()[0]

        # Total Balance
        cursor.execute("SELECT SUM(balance) FROM accounts")
        total_balance = cursor.fetchone()[0] or 0

        # Account Types
        cursor.execute("""
            SELECT account_type, COUNT(*)
            FROM accounts
            GROUP BY account_type
        """)
        account_type_counts = cursor.fetchall()

        print("\n--- Dashboard Summary ---")
        print(f"Total Customers: {total_customers}")
        print(f"Total Accounts: {total_accounts}")
        print(f"Total Bank Balance: ₹{total_balance:.2f}")
        print("Accounts by Type:")
        for acc_type, count in account_type_counts:
            print(f"  {acc_type}: {count}")

    except Exception as e:
        print("Error fetching dashboard summary:", e)
    finally:
        conn.close()
