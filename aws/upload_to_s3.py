import sqlite3
import boto3
import pandas as pd
import os

# AWS Configuration
AWS_REGION = "eu-central-1"  # Adjust if needed
BUCKET_PREFIX = "fin-data-pipeline"
bronze_bucket = f"{BUCKET_PREFIX}-bronze"
silver_bucket = f"{BUCKET_PREFIX}-silver"
gold_bucket = f"{BUCKET_PREFIX}-gold"

# S3 Client
s3 = boto3.client("s3")

# SQLite Database Connection
db_path = "transactions_pipeline.db"
conn = sqlite3.connect(db_path)

def upload_table_to_s3(table_name, bucket_name):
    """Extracts table from SQLite3, saves as Parquet, and uploads to S3."""
    print(f"🔹 Processing {table_name}...")

    # Load data from SQLite3
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    if df.empty:
        print(f"⚠️ No data found in {table_name}. Skipping upload.")
        return

    # Save as Parquet file
    file_path = f"data/{table_name}.parquet"
    df.to_parquet(file_path, index=False)

    # Upload to S3
    s3_key = f"{table_name}/{table_name}.parquet"
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"✅ {table_name} uploaded to S3 bucket: {bucket_name}/{s3_key}")

# Upload each table to its corresponding S3 bucket
upload_table_to_s3("bronze", bronze_bucket)
upload_table_to_s3("silver", silver_bucket)
upload_table_to_s3("gold", gold_bucket)

# Close connection
conn.close()
print("🚀 Data upload to S3 completed!")
