import os
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = "ap-south-1"

def upload_to_live_s3():
    bucket_name = "telco-enterprise-data-warehouse-2026"
    s3_client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION
    )
    
    try:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print(f"Successfully created S3 bucket in Mumbai: {bucket_name}")
    except Exception as e:
        print(f"Bucket note: {e} (Proceeding to upload)")

    star_schema_files = [
        "dim_office.csv", 
        "dim_team.csv", 
        "dim_product.csv", 
        "dim_employee.csv", 
        "dim_customer.csv", 
        "fact_call_transactions.csv"
    ]
    
    for file_name in star_schema_files:
        if os.path.exists(file_name):
            try:
                s3_client.upload_file(file_name, bucket_name, f"raw/{file_name}")
                print(f"Successfully uploaded {file_name} to s3://{bucket_name}/raw/{file_name}")
            except NoCredentialsError:
                print("AWS credentials were rejected or missing.")
            except Exception as e:
                print(f"Error uploading {file_name}: {e}")
        else:
            print(f"File {file_name} not found locally.")

if __name__ == "__main__":
    upload_to_live_s3()
