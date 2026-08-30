from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
import pandas as pd

# 1. Initialize Presidio Engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def mask_sensitive_data(text):
    # Analyze text to find PII using a balanced confidence threshold
    results = analyzer.analyze(text=str(text), 
                               entities=["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS"], 
                               language='en',
                               score_threshold=0.3)
    
    anonymized_result = anonymizer.anonymize(text=str(text), analyzer_results=results)
    return anonymized_result.text

# 2. Load the new 50,000-row advanced dataset
print("Loading 50,000 raw enterprise records...")
df = pd.read_csv('telco_signups_advanced_fraud.csv')

print("Applying Microsoft Presidio PII masking to Name, Email, and Phone columns...")
# Apply the privacy mask line-by-line
df['Name'] = df['Name'].apply(mask_sensitive_data)
df['Email'] = df['Email'].apply(mask_sensitive_data)
df['Phone'] = df['Phone'].apply(mask_sensitive_data)

# 3. Save the enterprise masked dataset
output_filename = 'telco_signups_advanced_masked.csv'
df.to_csv(output_filename, index=False)
print(f"Privacy layer execution complete! Saved masked enterprise dataset as '{output_filename}'.")