import sqlite3

def get_connection():
    """Connect to the SQLite database (creates bank.db if not exists)."""
    return sqlite3.connect('bank.db')

def initialize_database():
    """Create tables by executing schema.sql."""
    with open('schema.sql', 'r') as f:
        schema = f.read()
    conn = get_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()