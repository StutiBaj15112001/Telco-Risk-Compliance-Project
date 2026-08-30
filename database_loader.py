import pandas as pd
import sqlite3

# 1. Load the 50,000-row masked enterprise dataset
print("Loading masked enterprise dataset...")
df = pd.read_csv('telco_signups_advanced_masked.csv')

# 2. Connect to the local SQLite database
conn = sqlite3.connect('telco_data.db')
cursor = conn.cursor()

# 3. Load the DataFrame into the SQL table
print("Ingesting data into SQLite table 'customer_signups'...")
df.to_sql('customer_signups', conn, if_exists='replace', index=False)

# 4. Verify record count and fraud risk distribution via SQL
query_count = "SELECT COUNT(*) FROM customer_signups;"
total_records = pd.read_sql(query_count, conn).iloc[0, 0]

query_fraud = "SELECT Fraud_Risk_Flag, COUNT(*) as Count FROM customer_signups GROUP BY Fraud_Risk_Flag;"
fraud_breakdown = pd.read_sql(query_fraud, conn)

print(f"Successfully loaded {total_records} records into the database!")
print("\nFraud Risk Breakdown in Database:")
print(fraud_breakdown)

# 5. Close connection
conn.close()