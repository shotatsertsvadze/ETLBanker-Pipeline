





provider "aws" {
  region = "eu-central-1"  # Change this to your AWS region
}

# Use existing S3 buckets instead of creating new ones
data "aws_s3_bucket" "bronze" {
  bucket = "fin-data-pipeline-bronze"
}

data "aws_s3_bucket" "silver" {
  bucket = "fin-data-pipeline-silver"
}

data "aws_s3_bucket" "gold" {
  bucket = "fin-data-pipeline-gold"
}

# ✅ Fix: Declare the IAM role so Terraform recognizes it
data "aws_iam_role" "lambda_role" {
  name = "lambda-s3-role"
}


resource "aws_lambda_function" "bronze_to_silver" {
  function_name    = "bronze-to-silver-lambda"
  filename         = "../aws/lambda/bronze_to_silver.zip"  # Ensure this path is correct
  role             = data.aws_iam_role.lambda_role.arn
  handler          = "bronze_to_silver.lambda_handler"
  runtime          = "python3.12"

  source_code_hash = filebase64sha256("../aws/lambda/bronze_to_silver.zip")

  lifecycle {
    ignore_changes = [filename]
  }
}

resource "aws_lambda_function" "silver_to_gold" {
  function_name    = "silver-to-gold-lambda"
  filename         = "../aws/lambda/silver_to_gold.zip"  # Ensure this path is correct
  role             = data.aws_iam_role.lambda_role.arn
  handler          = "silver_to_gold.lambda_handler"
  runtime          = "python3.12"

  source_code_hash = filebase64sha256("../aws/lambda/silver_to_gold.zip")

  lifecycle {
    ignore_changes = [filename]
  }
}
