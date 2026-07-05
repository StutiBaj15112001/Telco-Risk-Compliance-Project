from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
import pandas as pd

# 1. Initialize the Engines
# The Analyzer "reads" the text to find PII.
# The Anonymizer "masks" the PII.
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def mask_sensitive_data(text):
    # Analyze the text to find sensitive information
    results = analyzer.analyze(text=text, entities=["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS"], language='en')
    
    # Anonymize (Mask) the found information
    anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results)
    
    return anonymized_result.text

# 2. Load our raw data from Phase 1
df = pd.read_csv('telco_signups.csv')

# 3. Apply the masking to specific columns
# We process the Name, Email, and Phone columns
df['Name'] = df['Name'].apply(mask_sensitive_data)
df['Email'] = df['Email'].apply(mask_sensitive_data)
df['Phone'] = df['Phone'].apply(mask_sensitive_data)

# 4. Save the cleaned/masked data
df.to_csv('telco_signups_masked.csv', index=False)
print("Privacy layer complete! Saved as 'telco_signups_masked.csv'.")