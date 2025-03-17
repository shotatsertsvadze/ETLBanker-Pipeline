import pandas as pd

# Create sample transaction data
data = {
    "transaction_id": [1, 2, 3],
    "customer_id": [101, 102, 103],
    "timestamp": ["2025-03-17 12:00:00", "2025-03-17 12:05:00", "2025-03-17 12:10:00"],
    "amount": [100.50, 200.75, 50.25],
    "transaction_type": ["deposit", "withdrawal", "payment"]
}

df = pd.DataFrame(data)

# Save as a Parquet file
df.to_parquet("testfile.parquet", index=False)

print("✅ Test Parquet file created: testfile.parquet")
