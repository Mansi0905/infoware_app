import sqlite3

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "db", "inventory.db")

def create_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = create_connection()
    cursor = conn.cursor()

    # Operator table
    cursor.execute('''CREATE TABLE IF NOT EXISTS operator (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')

    # Product master
    cursor.execute('''CREATE TABLE IF NOT EXISTS product_master (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT, sku_id TEXT, category TEXT, subcategory TEXT,
        image_path TEXT, name TEXT, description TEXT,
        tax REAL, price REAL, unit TEXT
    )''')

    # Goods receiving
    cursor.execute('''CREATE TABLE IF NOT EXISTS goods_receiving (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER, supplier TEXT,
        quantity INTEGER, unit TEXT,
        rate_per_unit REAL, total REAL, tax REAL,
        FOREIGN KEY(product_id) REFERENCES product_master(id)
    )''')

    # Sales
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER, customer TEXT,
        quantity INTEGER, unit TEXT,
        rate_per_unit REAL, total REAL, tax REAL,
        FOREIGN KEY(product_id) REFERENCES product_master(id)
    )''')

    # Default users
    cursor.execute("SELECT COUNT(*) FROM operator")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO operator (username, password) VALUES (?, ?)", ("operator1", "password1"))
        cursor.execute("INSERT INTO operator (username, password) VALUES (?, ?)", ("operator2", "password2"))

    conn.commit()
    conn.close()

# Run this only once
if __name__ == "__main__":
    initialize_db()
