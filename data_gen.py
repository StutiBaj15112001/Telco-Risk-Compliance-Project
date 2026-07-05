import pandas as pd # Import pandas to handle the table/CSV
from faker import Faker # Import Faker to generate fake data
import random # Import random to simulate "messy" data variations

# Initialize the Faker generator for Australian context
fake = Faker('en_AU') 

def generate_data(num_rows=1000):
    data = []
    for _ in range(num_rows):
        # 1. Generate fake identity info
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        
        # 2. Fraud Indicators (Simulating "messy/fraudulent" data)
        # We simulate a "fast completion" time (bots are fast)
        completion_time = random.randint(5, 300) 
        
        # We simulate an IP address (sometimes we force a repeated IP to look suspicious)
        ip = fake.ipv4() if random.random() > 0.05 else "192.168.1.1" 
        
        data.append([name, email, phone, completion_time, ip])
        
    # 3. Create the table
    return pd.DataFrame(data, columns=['Name', 'Email', 'Phone', 'Completion_Time', 'IP'])

# 4. Run the function and save as a CSV file
df = generate_data(1000)
df.to_csv('telco_signups.csv', index=False)

print("Data generation complete! You should see 'telco_signups.csv' in your folder.")