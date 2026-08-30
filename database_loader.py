import pandas as pd
import sqlite3

# 1. Load our masked data from Phase 2
print("Loading masked data...")
df = pd.read_csv('telco_signups_masked.csv')

# 2. Connect to a local SQLite database
# This will automatically create a file named 'telco_data.db' in your folder
conn = sqlite3.connect('telco_data.db')
cursor = conn.cursor()

# 3. Load the DataFrame directly into a SQL table named 'customer_signups'
# 'if_exists="replace"' means if you run this script again, it safely updates the table.
df.to_sql('customer_signups', conn, if_exists='replace', index=False)

print("Data successfully loaded into the SQL database table 'customer_signups'!")

# 4. Write a quick test SQL query to verify it works
# Let's count how many total rows we have in our database table
query = "SELECT COUNT(*) FROM customer_signups;"
result = pd.read_sql(query, conn)
print(f"Total records in SQL Database: {result.iloc[0, 0]}")

# 5. Close the database connection (best practice)
conn.close()