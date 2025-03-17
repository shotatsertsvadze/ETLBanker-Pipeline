import json
import boto3
import pandas as pd
from io import BytesIO

# AWS Configuration
s3 = boto3.client("s3")
BUCKET_PREFIX = "fin-data-pipeline"

def lambda_handler(event, context):
    """Triggered when a file is uploaded to the Bronze bucket."""
    for record in event["Records"]:
        bronze_bucket = f"{BUCKET_PREFIX}-bronze"
        silver_bucket = f"{BUCKET_PREFIX}-silver"

        # Get the uploaded file name
        key = record["s3"]["object"]["key"]

        # Download the file from Bronze S3 bucket
        response = s3.get_object(Bucket=bronze_bucket, Key=key)
        df = pd.read_parquet(BytesIO(response["Body"].read()))

        # Data Cleaning (remove nulls, duplicates, invalid amounts)
        df_cleaned = df.dropna().drop_duplicates()
        df_cleaned = df_cleaned[df_cleaned["amount"] > 0]

        # Save the cleaned data
        buffer = BytesIO()
        df_cleaned.to_parquet(buffer, index=False)
        buffer.seek(0)

        # Upload to Silver bucket
        s3.put_object(Bucket=silver_bucket, Key=key, Body=buffer.getvalue())

        print(f"✅ Processed {key}: Bronze → Silver")

    return {"statusCode": 200, "body": json.dumps("Success")}
