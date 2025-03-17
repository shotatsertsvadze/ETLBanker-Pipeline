import pandas as pd
import random
import uuid
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define parameters
num_records = 30000
transaction_types = ["deposit", "withdrawal", "transfer", "payment", "refund"]
payment_methods = ["credit_card", "debit_card", "bank_transfer", "cash"]
categories = ["food", "entertainment", "shopping", "bills", "travel", "healthcare"]
statuses = ["successful", "failed", "pending"]
locations = ["New York", "London", "Berlin", "Tokyo", "Paris", "Sydney", "Toronto"]

# Generate dataset
transactions = []
for _ in range(num_records):
    transaction_id = str(uuid.uuid4())
    customer_id = random.randint(10000, 99999)
    timestamp = fake.date_time_between(start_date="-6m", end_date="now")
    amount = round(random.uniform(1.00, 5000.00), 2)
    transaction_type = random.choice(transaction_types)
    merchant = fake.company() if transaction_type == "payment" else None
    category = random.choice(categories) if transaction_type == "payment" else None
    payment_method = random.choice(payment_methods)
    status = random.choice(statuses)
    location = random.choice(locations)

    transactions.append([transaction_id, customer_id, timestamp, amount, transaction_type,
                         merchant, category, payment_method, status, location])

# Create DataFrame
columns = ["transaction_id", "customer_id", "timestamp", "amount", "transaction_type",
           "merchant", "category", "payment_method", "status", "location"]
df = pd.DataFrame(transactions, columns=columns)

# Save as Parquet
df.to_parquet("data/synthetic_transactions.parquet", index=False)

print("✅ Synthetic dataset generated: data/synthetic_transactions.parquet")
