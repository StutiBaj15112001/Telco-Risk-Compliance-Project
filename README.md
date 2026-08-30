# 🛡️ Telco Operational Risk & Compliance Platform

An automated, end-to-end data engineering and risk mitigation platform built to ensure strict compliance with Australian Privacy Principles (APP) while actively detecting synthetic identity fraud and automated bot signups in telecommunications.

## 🚀 Business Problem & Context
Telecommunication providers face dual operational pressures:
1. **Regulatory Compliance Risk:** Ingesting and analyzing customer acquisition streams exposes companies to massive legal and financial liabilities if Personally Identifiable Information (PII) is mishandled.
2. **Fraud & Risk Exposure:** Sophisticated bad actors utilize automated bots to rapidly create fraudulent profiles, increasing bad-debt and compliance audit costs.

## ⚙️ Solution Architecture & Workflow
This platform implements a robust Modern Data Pipeline (ETL):
1. **Data Ingestion (Data Engineering):** Generates and ingests large-scale synthetic customer sign-up records containing embedded anomalies (velocity and IP reuse patterns).
2. **Data Governance & Privacy Layer:** Utilizes **Microsoft Presidio** and natural language processing (`spaCy`) to perform automated Named Entity Recognition (NER), securing high-risk PII (Names, Phones, Emails) before analytics processing.
3. **Database Storage (SQL):** Loads clean, structured data into a persistent relational database (`SQLite`) using automated scripts.
4. **Risk Intelligence & Visualization:** Deploys an interactive executive dashboard (**Streamlit**) providing real-time visibility into compliance metrics, total signups, and high-risk bot flags.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Engineering & Manipulation:** Pandas, SQLite, SQL
* **Data Governance / Privacy:** Microsoft Presidio, spaCy (NER)
* **Visualization & Frontend:** Streamlit
* **Version Control:** Git & GitHub

## 📊 Key Features & Dashboard Highlights
* **Automated PII Redaction:** Successfully scrubs customer records on ingestion, maintaining a secure data lineage.
* **Behavioral Risk Scoring:** Identifies abnormal form completion speeds (<30s) to flag potential automated bot submissions for human review.
* **Role-Based Insights:** Separates high-level business analytics from sensitive data handling.

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/Telco-Risk-Compliance-Project.git](https://github.com/your-username/Telco-Risk-Compliance-Project.git)
