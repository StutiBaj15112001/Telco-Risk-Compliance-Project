import sqlite3

conn = sqlite3.connect('telco_enterprise.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT o.city, t.team_name, COUNT(f.transaction_id) as total_calls, 
           ROUND(AVG(f.fraud_risk_flag)*100, 2) as fraud_rate_pct
    FROM fact_call_transactions f
    JOIN dim_office o ON f.office_id = o.office_id
    JOIN dim_team t ON f.team_id = t.team_id
    GROUP BY o.city, t.team_name
    ORDER BY fraud_rate_pct DESC
    LIMIT 5;
""")

for row in cursor.fetchall():
    print(row)

conn.close()