import json
import boto3
import pandas as pd
from io import BytesIO

# AWS Configuration
s3 = boto3.client("s3")
BUCKET_PREFIX = "fin-data-pipeline"

def lambda_handler(event, context):
    """Triggered when a file is uploaded to the Silver bucket."""
    for record in event["Records"]:
        silver_bucket = f"{BUCKET_PREFIX}-silver"
        gold_bucket = f"{BUCKET_PREFIX}-gold"

        key = record["s3"]["object"]["key"]

        # Download the file from Silver S3 bucket
        response = s3.get_object(Bucket=silver_bucket, Key=key)
        df = pd.read_parquet(BytesIO(response["Body"].read()))

        # Data Aggregation
        df_aggregated = df.groupby("customer_id").agg(
            total_transactions=("transaction_id", "count"),
            total_amount=("amount", "sum"),
            avg_transaction_amount=("amount", "mean")
        ).reset_index()

        # Save the aggregated data
        buffer = BytesIO()
        df_aggregated.to_parquet(buffer, index=False)
        buffer.seek(0)

        # Upload to Gold bucket
        s3.put_object(Bucket=gold_bucket, Key=key, Body=buffer.getvalue())

        print(f"✅ Processed {key}: Silver → Gold")

    return {"statusCode": 200, "body": json.dumps("Success")}
