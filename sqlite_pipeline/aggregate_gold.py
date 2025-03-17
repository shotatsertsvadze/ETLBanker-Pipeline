import sqlite3

conn = sqlite3.connect("transactions_pipeline.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO gold
SELECT 
    customer_id,
    COUNT(transaction_id),
    SUM(amount),
    AVG(amount),
    SUM(CASE WHEN status = 'successful' THEN 1 ELSE 0 END),
    SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END)
FROM silver
GROUP BY customer_id
""")

conn.commit()
conn.close()

print("✅ Aggregated data inserted into Gold table!")
