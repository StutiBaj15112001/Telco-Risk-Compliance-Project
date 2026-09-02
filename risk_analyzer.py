import os
import pandas as pd
from sqlalchemy import create_engine

DB_HOST = "telco-risk-warehouse.cbyiay28mblp.ap-south-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "RekhaBaj1!"
DB_PORT = "5432"

def run_risk_compliance_analytics():
    connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)
    
    print("Executing Risk & Compliance validation queries on AWS RDS warehouse...\n")
    
    query_risk_summary = """
        SELECT 
            p.product_type,
            COUNT(f.transaction_id) as total_calls,
            SUM(f.call_duration_minutes) as total_duration_min,
            AVG(f.call_duration_minutes) as avg_duration_min
        FROM fact_call_transactions f
        JOIN dim_product p ON f.product_id = p.product_id
        GROUP BY p.product_type
        ORDER BY total_calls DESC;
    """
    
    df_summary = pd.read_sql(query_risk_summary, engine)
    print("--- Product Call Volume & Usage Summary ---")
    print(df_summary)
    print("\n" + "="*50 + "\n")
    
    query_compliance_audit = """
        SELECT 
            f.transaction_id,
            c.name as customer_name,
            e.agent_name as employee_name,
            f.call_duration_minutes,
            f.fraud_risk_flag
        FROM fact_call_transactions f
        JOIN dim_customer c ON f.customer_id = c.customer_id
        JOIN dim_employee e ON f.employee_id = e.employee_id
        ORDER BY f.call_duration_minutes DESC
        LIMIT 5;
    """
    
    df_audit = pd.read_sql(query_compliance_audit, engine)
    print("--- Top 5 Longest Call Transactions for Audit ---")
    print(df_audit)

if __name__ == "__main__":
    run_risk_compliance_analytics()