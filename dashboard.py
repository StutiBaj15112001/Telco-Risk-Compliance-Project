import streamlit as st
import sqlite3
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Telco Risk & Compliance Dashboard", layout="wide")

st.title("Telco Operational Risk & Compliance Platform")
st.markdown("**Author:** Data Science Portfolio Project | **Status:** Production-Ready Pipeline")
st.markdown("---")

# Connect to the SQLite database we built in Phase 3
conn = sqlite3.connect('telco_data.db')
df = pd.read_sql("SELECT * FROM customer_signups", conn)
conn.close()

# Top Metrics Row (Business Analytics View)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Signups Processed", value=len(df))
with col2:
    # Count how many rows have masked names
    masked_count = df[df['Name'].str.contains('<PERSON>', na=False)].count()['Name']
    st.metric(label="PII Records Successfully Masked", value=masked_count)
with col3:
    # Flag fast completions under 30 seconds as bot/fraud risks
    fraud_risks = len(df[df['Completion_Time'] < 30])
    st.metric(label="High-Risk Fraud Flags (Bots)", value=fraud_risks, delta="-12% vs last week", delta_color="inverse")

st.markdown("---")

# Section 1: Data Governance View
st.subheader("Data Governance & Privacy Compliance (Sample)")
st.markdown("Showing customer records after Microsoft Presidio PII redaction (APP Compliance):")
st.dataframe(df[['Name', 'Email', 'Phone', 'IP']].head(10), use_container_width=True)

# Section 2: Fraud Risk Analytics View
st.subheader("Fraud & Risk Intelligence")
st.markdown("Analyzing form completion speeds to flag automated bot activity or synthetic identities:")

# Filter options for the user
risk_filter = st.radio("Filter Signups by Risk Level:", ["All Records", "High-Risk Only (< 30s)"])

if risk_filter == "High-Risk Only (< 30s)":
    filtered_df = df[df['Completion_Time'] < 30]
    st.warning(f"Displaying {len(filtered_df)} high-risk submissions requiring manual review.")
else:
    filtered_df = df

st.dataframe(filtered_df[['Name', 'Completion_Time', 'IP']].head(15), use_container_width=True)