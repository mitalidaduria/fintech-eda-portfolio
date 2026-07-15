# FinTech Payment Fraud Anomaly Detection

## Executive Summary
This repository contains an exploratory data analysis (EDA) of financial transaction logs to identify primary drivers of payment anomalies and fraudulent behavior. 

**Key Findings:**
* **Imbalanced Threat Profile:** Fraud represents less than  of total transaction volume, requiring highly sensitive anomaly detection rather than standard classification.
* **Vector Isolation:** Anomalous activity is heavily concentrated in specific transaction vectors, primarily 
* **Balance Irregularities:** Fraudulent events frequently correlate with accounts draining their total balance to zero in a single transaction.

## Business Impact & Strategic Recommendations
If current rule-based systems apply blanket holds on high-value transfers, the business risks significant false positives, increasing customer friction. 

**Next Steps for the Data Product Team:**
1. **Dynamic Thresholding:** Implement monitoring dashboards that track  velocity rather than static amount limits.
2. **Feature Engineering Pipeline:** Begin engineering temporal features (e.g., time-since-last-login) to combine with transactional data for a more robust machine learning classification model.

## Repository Structure
* `/data/`: Contains dataset schema documentation (Raw CSV excluded via .gitignore due to volume).
* `/analysis/`: Contains Jupyter notebooks with full profiling, time-series, and statistical analysis.
* `FINDINGS.md`: Detailed breakdown of data quality issues and technical charts.
