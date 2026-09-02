import os
import pandas as pd
from sqlalchemy import create_engine

DB_HOST = "telco-risk-warehouse.cbyiay28mblp.ap-south-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "RekhaBaj1!"
DB_PORT = "5432"

def load_star_schema_to_rds():
    connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)
    
    tables = [
        "dim_office", 
        "dim_team", 
        "dim_product", 
        "dim_employee", 
        "dim_customer", 
        "fact_call_transactions"
    ]

    for table in tables:
        file_path = f"{table}.csv"
        if os.path.exists(file_path):
            print(f"Processing local file: {file_path}")
            df = pd.read_csv(file_path)
            
            print(f"Writing {table} to AWS RDS PostgreSQL...")
            df.to_sql(table, engine, if_exists='replace', index=False)
            print(f"Successfully populated table: {table}")
        else:
            print(f"Warning: Local file {file_path} not found.")

if __name__ == "__main__":
    load_star_schema_to_rds()