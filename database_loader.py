import sqlite3
import pandas as pd

def load_data_to_sqlite():
    # Connect to SQLite database (creates telco_enterprise.db)
    conn = sqlite3.connect("telco_enterprise.db")
    cursor = conn.cursor()

    # List of CSV files to load corresponding to our star schema
    tables = {
        "dim_office": "dim_office.csv",
        "dim_team": "dim_team.csv",
        "dim_product": "dim_product.csv",
        "dim_employee": "dim_employee.csv",
        "dim_customer": "dim_customer.csv",
        "fact_call_transactions": "fact_call_transactions.csv"
    }

    for table_name, file_name in tables.items():
        print(f"Loading {file_name} into table '{table_name}'...")
        df = pd.read_csv(file_name)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    print("Database loading complete. All 6 relational tables successfully created in 'telco_enterprise.db'.")

if __name__ == "__main__":
    load_data_to_sqlite()