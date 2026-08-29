# Data Dictionary: Telco Customer Signups

This dataset contains synthetic customer acquisition data generated for the purpose of privacy testing and fraud detection modeling.

| Column Name | Data Type | Description | PII Status |
| :--- | :--- | :--- | :--- |
| **Name** | String | Full name of the customer. | High (PII) |
| **Email** | String | Customer contact email address. | High (PII) |
| **Phone** | String | Customer contact phone number. | High (PII) |
| **Completion_Time**| Integer | Time taken to complete the form (in seconds). | None |
| **IP** | String | The IP address from which the signup originated. | Medium |

---
*Note: This dataset is entirely synthetic and was generated using the Faker library.*