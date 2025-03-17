import sqlite3

# Connect to SQLite3
conn = sqlite3.connect("transactions_pipeline.db")
cursor = conn.cursor()

# Create tables
create_bronze_table = """
CREATE TABLE IF NOT EXISTS bronze (
    transaction_id TEXT PRIMARY KEY,
    customer_id INTEGER,
    timestamp TEXT,
    amount REAL,
    transaction_type TEXT,
    merchant TEXT,
    category TEXT,
    payment_method TEXT,
    status TEXT,
    location TEXT
);
"""

create_silver_table = """
CREATE TABLE IF NOT EXISTS silver (
    transaction_id TEXT PRIMARY KEY,
    customer_id INTEGER,
    timestamp TEXT,
    amount REAL CHECK(amount > 0),
    transaction_type TEXT,
    merchant TEXT,
    category TEXT,
    payment_method TEXT,
    status TEXT,
    location TEXT
);
"""

create_gold_table = """
CREATE TABLE IF NOT EXISTS gold (
    customer_id INTEGER PRIMARY KEY,
    total_transactions INTEGER,
    total_amount REAL,
    avg_transaction_amount REAL,
    num_successful_transactions INTEGER,
    num_failed_transactions INTEGER
);
"""

# Execute table creation
cursor.execute(create_bronze_table)
cursor.execute(create_silver_table)
cursor.execute(create_gold_table)

# Commit and close
conn.commit()
conn.close()

print("✅ SQLite3 database and tables created!")
