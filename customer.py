from db import get_connection
from colorama import Fore, Style

def create_customer(name, email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        conn.commit()
        print(Fore.GREEN + f"✅ Customer '{name}' created successfully." + Style.RESET_ALL)
    except Exception as e:
        if "UNIQUE constraint failed: customers.email" in str(e):
            print(Fore.RED + f"❌ A customer with the email '{email}' already exists." + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Error: " + str(e) + Style.RESET_ALL)
    finally:
        conn.close()

def get_customer_id(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id FROM customers WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def list_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id, name, email, phone FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return customers

def delete_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM accounts WHERE customer_id = ?", (customer_id,))
        if cursor.fetchall():
            print(Fore.RED + "❌ Customer has associated accounts. Delete them first." + Style.RESET_ALL)
            return False

        cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
        conn.commit()
        print(Fore.GREEN + "✅ Customer deleted successfully." + Style.RESET_ALL)
        return True
    except Exception as e:
        print(Fore.RED + "❌ Error deleting customer: " + str(e) + Style.RESET_ALL)
        return False
    finally:
        conn.close()

def delete_customer_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT customer_id, name FROM customers WHERE email = ?", (email,))
        result = cursor.fetchone()
        if not result:
            print(Fore.RED + "❌ Customer not found." + Style.RESET_ALL)
            return False
        customer_id, customer_name = result

        cursor.execute("SELECT account_id FROM accounts WHERE customer_id = ?", (customer_id,))
        accounts = cursor.fetchall()

        for acc in accounts:
            cursor.execute("DELETE FROM transactions WHERE account_id = ?", (acc[0],))
            cursor.execute("DELETE FROM accounts WHERE account_id = ?", (acc[0],))

        cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
        conn.commit()
        print(Fore.GREEN + f"✅ Customer '{customer_name}' and related accounts deleted successfully." + Style.RESET_ALL)
        return True
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}" + Style.RESET_ALL)
        return False
    finally:
        conn.close()
