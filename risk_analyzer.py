import os
import pandas as pd
from sqlalchemy import create_engine

DB_HOST = "telco-risk-warehouse.cbyiay28mblp.ap-south-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "RekhaBaj1!"
DB_PORT = "5432"

def run_comprehensive_risk_and_performance_analysis():
    connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)
    
    print("Executing Comprehensive Risk, Fraud, & Team Performance Analytics...\n")
    
    # 1. Product Call Volume & Usage Summary
    query_risk_summary = """
        SELECT 
            p.product_type,
            COUNT(f.transaction_id) as total_calls,
            SUM(f.call_duration_minutes) as total_duration_min,
            ROUND(CAST(AVG(f.call_duration_minutes) AS NUMERIC), 2) as avg_duration_min
        FROM fact_call_transactions f
        JOIN dim_product p ON f.product_id = p.product_id
        GROUP BY p.product_type
        ORDER BY total_calls DESC;
    """
    df_summary = pd.read_sql(query_risk_summary, engine)
    print("--- Product Call Volume & Usage Summary ---")
    print(df_summary.to_string(index=False))
    print("\n" + "="*50 + "\n")
    
    # 2. Top 5 Longest Call Transactions for Audit
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
    print(df_audit.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 3. Fraud Risk Analysis by Operational Team
    query_fraud_by_team = """
        SELECT 
            t.team_name,
            COUNT(f.transaction_id) as total_calls,
            SUM(f.fraud_risk_flag) as fraud_cases,
            ROUND(CAST(SUM(f.fraud_risk_flag) AS NUMERIC) * 100.0 / COUNT(f.transaction_id), 2) as fraud_percentage
        FROM fact_call_transactions f
        JOIN dim_team t ON f.team_id = t.team_id
        GROUP BY t.team_name
        ORDER BY fraud_percentage DESC;
    """
    df_fraud = pd.read_sql(query_fraud_by_team, engine)
    print("--- Fraud Risk Analysis by Operational Team ---")
    print(df_fraud.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 4. Team Performance & Operational Efficiency
    query_team_performance = """
        SELECT 
            t.team_name,
            COUNT(f.transaction_id) as total_calls,
            ROUND(CAST(AVG(f.call_duration_minutes) AS NUMERIC), 2) as avg_duration_min,
            ROUND(CAST(AVG(f.completion_time_seconds) AS NUMERIC), 2) as avg_completion_sec,
            ROUND(CAST(SUM(f.is_transferred) AS NUMERIC) * 100.0 / COUNT(f.transaction_id), 2) as transfer_rate_pct
        FROM fact_call_transactions f
        JOIN dim_team t ON f.team_id = t.team_id
        GROUP BY t.team_name
        ORDER BY total_calls DESC;
    """
    df_team = pd.read_sql(query_team_performance, engine)
    print("--- Operational Team Performance & Efficiency Summary ---")
    print(df_team.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 5. Top 5 Agents by Handling Volume
    query_top_agents = """
        SELECT 
            e.agent_name,
            t.team_name,
            COUNT(f.transaction_id) as total_handled_calls,
            SUM(f.fraud_risk_flag) as fraud_incidents
        FROM fact_call_transactions f
        JOIN dim_employee e ON f.employee_id = e.employee_id
        JOIN dim_team t ON f.team_id = t.team_id
        GROUP BY e.agent_name, t.team_name
        ORDER BY total_handled_calls DESC
        LIMIT 5;
    """
    df_agents = pd.read_sql(query_top_agents, engine)
    print("--- Top 5 Agents by Handling Volume ---")
    print(df_agents.to_string(index=False))

if __name__ == "__main__":
    run_comprehensive_risk_and_performance_analysis()