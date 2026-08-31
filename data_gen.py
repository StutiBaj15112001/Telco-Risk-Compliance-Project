import csv
import random
from datetime import datetime, timedelta

def generate_enterprise_data():
    # Setup offices across major Australian hubs
    offices = [
        {"office_id": 1, "city": "Melbourne", "state": "VIC", "timezone": "AEST"},
        {"office_id": 2, "city": "Sydney", "state": "NSW", "timezone": "AEST"},
        {"office_id": 3, "city": "Brisbane", "state": "QLD", "timezone": "AEST"},
        {"office_id": 4, "city": "Perth", "state": "WA", "timezone": "AWST"},
        {"office_id": 5, "city": "Adelaide", "state": "SA", "timezone": "ACST"}
    ]

    # Setup specialized operational teams including Mobile Faults and BOH
    teams = [
        {"team_id": 1, "team_name": "Sales", "multiplier": 1.0},
        {"team_id": 2, "team_name": "NBN Assurance", "multiplier": 1.6},
        {"team_id": 3, "team_name": "Mobile Faults", "multiplier": 1.4},
        {"team_id": 4, "team_name": "Customer Service", "multiplier": 1.3},
        {"team_id": 5, "team_name": "Payments Assistance", "multiplier": 0.9},
        {"team_id": 6, "team_name": "Back of House (BOH)", "multiplier": 0.4},
        {"team_id": 7, "team_name": "Priority Assistance", "multiplier": 0.3},
        {"team_id": 8, "team_name": "Bereavement", "multiplier": 0.1}
    ]

    # Setup products
    products = [
        {"product_id": 1, "product_type": "5G Mobile Plan", "plan_tier": "Basic", "price": 45.0},
        {"product_id": 2, "product_type": "5G Mobile Plan", "plan_tier": "Essential", "price": 65.0},
        {"product_id": 3, "product_type": "5G Mobile Plan", "plan_tier": "Premium", "price": 95.0},
        {"product_id": 4, "product_type": "NBN Fixed Internet", "plan_tier": "Basic", "price": 70.0},
        {"product_id": 5, "product_type": "NBN Fixed Internet", "plan_tier": "NBN Standard", "price": 85.0},
        {"product_id": 6, "product_type": "NBN Fixed Internet", "plan_tier": "Premium", "price": 115.0}
    ]

    # Generate Employees (50 per office = 250 total agents)
    employees = []
    emp_id_counter = 1
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Sam", "Chris", "Pat", "Riley", "Casey", "Dakota",
                   "Aiden", "Liam", "Noah", "Emma", "Olivia", "Sophia", "Ava", "Isabella", "Lucas", "Mason"]
    last_names = ["Smith", "Jones", "Brown", "Wilson", "Taylor", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez",
                  "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Clark", "Lewis", "Lee", "Walker"]

    for office in offices:
        for _ in range(50):
            emp_name = f"{random.choice(first_names)} {random.choice(last_names)}"
            team = random.choice(teams)
            employees.append({
                "employee_id": emp_id_counter,
                "agent_name": emp_name,
                "office_id": office["office_id"],
                "team_id": team["team_id"],
                "hire_date": "2020-01-10"
            })
            emp_id_counter += 1

    # Generate Customers (5,000 unique profiles)
    customers = []
    for cust_id in range(1, 5001):
        c_name = f"Customer_{cust_id}"
        email = f"user_{cust_id}@example.com"
        account_type = random.choices(["Existing Account", "New Unrecognized Account"], weights=[0.75, 0.25])[0]
        ip_address = f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"
        region = random.choice(["VIC", "NSW", "QLD", "WA", "SA", "TAS"])
        customers.append({
            "customer_id": cust_id,
            "name": c_name,
            "email": email,
            "account_type": account_type,
            "ip_address": ip_address,
            "region": region
        })

    # Macro-fraud trend matrix mapping (Year, Quarter) -> Base Rate
    macro_fraud_matrix = {
        (2020, 1): 0.021, (2020, 2): 0.029, (2020, 3): 0.026, (2020, 4): 0.032,
        (2021, 1): 0.024, (2021, 2): 0.022, (2021, 3): 0.020, (2021, 4): 0.025,
        (2022, 1): 0.027, (2022, 2): 0.031, (2022, 3): 0.028, (2022, 4): 0.034,
        (2023, 1): 0.022, (2023, 2): 0.019, (2023, 3): 0.017, (2023, 4): 0.021,
        (2024, 1): 0.025, (2024, 2): 0.028, (2024, 3): 0.023, (2024, 4): 0.029,
        (2025, 1): 0.018, (2025, 2): 0.016, (2025, 3): 0.014, (2025, 4): 0.017,
        (2026, 1): 0.013, (2026, 2): 0.012, (2026, 3): 0.011, (2026, 4): 0.014
    }

    # Generate Fact Transactions (Timeline 2020 to 2026)
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2026, 8, 31)
    
    fact_calls = []
    transaction_id = 1
    
    current_date = start_date
    while current_date <= end_date:
        # Exclude Sundays (weekday() == 6)
        if current_date.weekday() != 6:
            year = current_date.year
            month = current_date.month
            q = (month - 1) // 3 + 1
            base_rate = macro_fraud_matrix.get((year, q), 0.015)
            
            # Day-of-week volume weighting (Monday peak 1.4x, Saturday lower)
            dow = current_date.weekday()
            volume_multipliers = {0: 1.4, 1: 1.1, 2: 1.0, 3: 1.0, 4: 0.8, 5: 0.7}
            daily_volume_factor = volume_multipliers.get(dow, 1.0)
            
            daily_calls = int(random.gauss(140, 18) * daily_volume_factor)
            
            for _ in range(daily_calls):
                # Operational hours strictly 08:00 to 19:00
                hour = random.randint(8, 18)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                call_timestamp = current_date.replace(hour=hour, minute=minute, second=second)
                
                customer = random.choice(customers)
                employee = random.choice(employees)
                product = random.choice(products)
                
                originating_team = next(t for t in teams if t["team_id"] == employee["team_id"])
                
                # Call duration modeling (5 minutes to 180 minutes long-tail)
                duration_minutes = int(random.lognormvariate(2.8, 0.6))
                duration_minutes = max(5, min(duration_minutes, 180))
                completion_time_seconds = duration_minutes * 60 + random.randint(-15, 45)
                
                is_transferred = random.random() < 0.22
                transfer_reason = random.choice(["Technical Escalation", "Fraud Verification", "Billing Dispute", "None"]) if is_transferred else "None"
                
                linked_accounts_count = random.choices([1, 2, 3, 5, 10, 25, 50], weights=[70, 15, 8, 4, 2, 1, 0.5])[0]
                
                # Dynamic quarterly & team fraud calculation
                team_weight = originating_team["multiplier"]
                account_weight = 1.8 if customer["account_type"] == "New Unrecognized Account" else 0.6
                final_probability = base_rate * team_weight * account_weight
                fraud_risk_flag = 1 if random.random() < final_probability else 0
                
                fact_calls.append({
                    "transaction_id": transaction_id,
                    "timestamp": call_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "year": year,
                    "quarter": q,
                    "customer_id": customer["customer_id"],
                    "employee_id": employee["employee_id"],
                    "office_id": employee["office_id"],
                    "team_id": employee["team_id"],
                    "product_id": product["product_id"],
                    "call_duration_minutes": duration_minutes,
                    "completion_time_seconds": max(10, completion_time_seconds),
                    "is_transferred": 1 if is_transferred else 0,
                    "transfer_reason": transfer_reason,
                    "linked_accounts_count": linked_accounts_count,
                    "fraud_risk_flag": fraud_risk_flag
                })
                transaction_id += 1
                
        current_date += timedelta(days=1)

    # Export dimension and fact tables to CSV files
    with open("dim_office.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["office_id", "city", "state", "timezone"])
        writer.writeheader()
        writer.writerows(offices)

    with open("dim_team.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["team_id", "team_name", "multiplier"])
        writer.writeheader()
        writer.writerows(teams)

    with open("dim_product.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["product_id", "product_type", "plan_tier", "price"])
        writer.writeheader()
        writer.writerows(products)

    with open("dim_employee.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["employee_id", "agent_name", "office_id", "team_id", "hire_date"])
        writer.writeheader()
        writer.writerows(employees)

    with open("dim_customer.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["customer_id", "name", "email", "account_type", "ip_address", "region"])
        writer.writeheader()
        writer.writerows(customers)

    with open("fact_call_transactions.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = list(fact_calls[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(fact_calls)

    print(f"Successfully generated star schema tables: {len(fact_calls)} multi-year enterprise records processed from 2020 to 2026.")

if __name__ == "__main__":
    generate_enterprise_data()