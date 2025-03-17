# **ETLBanker-Pipeline 🚀**

## 📌 Project Overview
This project is an **ETL Data Pipeline** built with **AWS, Terraform, and Python**. It automates data ingestion, transformation, and aggregation using **AWS Lambda, S3, and Terraform**.

✅ **Features:**
- **AWS S3** → Stores Bronze, Silver, and Gold layer data.
- **AWS Lambda** → Automates data transformation.
- **Terraform** → Manages AWS infrastructure as code.
- **Python & Pandas** → Handles data processing.

---
## 📂 Project Structure
```bash
ETLBanker-Pipeline/
│── data/                      # Data generation & ingestion
│   ├── generate_synthetic_data.py  # Creates test transaction data
│── aws/                       # AWS-related scripts
│   ├── lambda/                # AWS Lambda functions
│   ├── upload_to_s3.py        # Uploads processed data to S3
│── terraform/                 # Infrastructure as Code (Terraform)
│   ├── main.tf                # Terraform configuration file
│── sqlite_pipeline/           # Local ETL pipeline using SQLite3
│── README.md                  # Project documentation
│── .gitignore                 # Ignore unnecessary files
