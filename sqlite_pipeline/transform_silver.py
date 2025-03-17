import sqlite3

conn = sqlite3.connect("transactions_pipeline.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO silver
SELECT DISTINCT * FROM bronze
WHERE amount > 0
""")

conn.commit()
conn.close()

print("✅ Data transformed and inserted into Silver table!")
