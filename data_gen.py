import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('en_AU')

def generate_advanced_telco_fraud_data(num_rows=50000):
    data = []
    
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 8, 30)
    total_days = (end_date - start_date).days

    print(f"Generating {num_rows} advanced enterprise records with frontline Telstra fraud signatures...")

    for i in range(num_rows):
        if i > 0 and i % 10000 == 0:
            print(f"-> Processed {i} records...")

        # 1. Timeline & Seasonal Spikes (EOFY in June, Phone launches in Aug/Sep, Black Friday/Xmas in Nov/Dec)
        random_day_offset = random.randint(0, total_days)
        signup_date = start_date + timedelta(days=random_day_offset)
        month = signup_date.month
        is_peak_season = month in [6, 8, 9, 11, 12]
        
        # 2. Customer Identity (Using real innocent Australian details)
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        
        # 3. Product & Plan Selection (Fraudsters avoid NBN fixed plans; they want 5G mobile Essential/Premium)
        product_choices = ["NBN Fixed Internet", "5G Mobile Plan"]
        product_weights = [0.35, 0.65] # Higher mobile weight
        product_type = random.choices(product_choices, weights=product_weights, k=1)[0]
        
        if product_type == "5G Mobile Plan":
            plan_tier = random.choices(["Basic", "Essential", "Premium"], weights=[0.2, 0.4, 0.4], k=1)[0]
        else:
            plan_tier = "NBN Standard"

        # 4. Delivery Method (Fraudsters heavily favor eSIM via app for instant remote takeover)
        delivery_method = random.choices(["Physical SIM", "eSIM via App"], weights=[0.6, 0.4], k=1)[0]
        
        # 5. Account Characteristics (Fraudsters always use a brand-new account with high historical linkages)
        account_type = random.choices(["Existing Account", "New Unrecognized Account"], weights=[0.7, 0.3], k=1)[0]
        
        # Determine Fraud Likelihood based on your frontline rulebook
        # High fraud profile: New Account + eSIM via App + Essential/Premium Plan + Peak Season + 5G Mobile
        is_high_risk_profile = (
            account_type == "New Unrecognized Account" and 
            delivery_method == "eSIM via App" and 
            plan_tier in ["Essential", "Premium"] and 
            is_peak_season and 
            product_type == "5G Mobile Plan"
        )

        if is_high_risk_profile and random.random() < 0.65:
            # Fraud indicators triggered
            completion_time = random.randint(5, 25) # Bot-speed form entry
            linked_accounts_count = random.randint(5, 12) # Linked to multiple suspicious accounts
            voice_accent_anomaly = random.choice(["Yes - Voice Modulation Detected", "Yes - Accent Mismatch Suspected", "None"])
            ip = "192.168.1.1" # Clustered rogue IP
            fraud_risk_flag = 1 # Confirmed Synthetic Fraud Pattern
        else:
            # Normal customer behavior
            completion_time = random.randint(50, 600)
            linked_accounts_count = random.randint(0, 2)
            voice_accent_anomaly = "None"
            ip = fake.ipv4()
            fraud_risk_flag = 0

        data.append([
            signup_date.strftime('%Y-%m-%d'),
            name,
            email,
            phone,
            product_type,
            plan_tier,
            delivery_method,
            account_type,
            linked_accounts_count,
            voice_accent_anomaly,
            completion_time,
            ip,
            fraud_risk_flag
        ])

    columns = [
        'Signup_Date', 'Name', 'Email', 'Phone', 'Product_Type', 'Plan_Tier', 
        'Delivery_Method', 'Account_Type', 'Linked_Accounts_Count', 
        'Voice_Accent_Anomaly_Flag', 'Completion_Time', 'IP_Address', 'Fraud_Risk_Flag'
    ]
    return pd.DataFrame(data, columns=columns)

# Run and Save
df = advanced_data = generate_advanced_telco_fraud_data(50000)
df.to_csv('telco_signups_advanced_fraud.csv', index=False)
print("Advanced 50,000-row enterprise fraud dataset generated successfully as 'telco_signups_advanced_fraud.csv'!")