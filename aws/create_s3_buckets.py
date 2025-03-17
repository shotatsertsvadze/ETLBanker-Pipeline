import boto3

# AWS Configuration
AWS_REGION = "eu-central-1"  # Change to your preferred region
BUCKET_PREFIX = "fin-data-pipeline"  # Your unique project name

# Define bucket names
bronze_bucket = f"{BUCKET_PREFIX}-bronze"
silver_bucket = f"{BUCKET_PREFIX}-silver"
gold_bucket = f"{BUCKET_PREFIX}-gold"

# Initialize S3 client
s3 = boto3.client("s3")

def create_bucket(bucket_name):
    """Creates an S3 bucket in the specified AWS region."""
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": AWS_REGION}
        )
        print(f"✅ S3 Bucket Created: {bucket_name}")
    except Exception as e:
        print(f"⚠️ Error creating bucket {bucket_name}: {e}")

# Create buckets
create_bucket(bronze_bucket)
create_bucket(silver_bucket)
create_bucket(gold_bucket)
