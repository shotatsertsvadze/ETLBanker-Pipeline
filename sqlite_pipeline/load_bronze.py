import sqlite3
import pandas as pd

# Load dataset
df = pd.read_parquet("data/synthetic_transactions.parquet")

# Connect to SQLite3
conn = sqlite3.connect("transactions_pipeline.db")

# Insert into Bronze table
df.to_sql("bronze", conn, if_exists="append", index=False)

# Commit and close
conn.commit()
conn.close()

print("✅ Data loaded into Bronze table!")
