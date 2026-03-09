# Projects — Omkar Shashank Pathare

> End-to-end ML projects spanning NLP, computer vision, recommendation systems, big data engineering, time-series forecasting, and cloud MLOps.

**Author:** Omkar Shashank Pathare
**Affiliation:** M.S. Data Science, Stevens Institute of Technology (May 2026)
**Contact:** opathare@stevens.edu · [LinkedIn](https://www.linkedin.com/in/omkar-pathare-337a59234) · [Portfolio](https://coderx-com.github.io/Portfolio)

---

## Repository Structure

```
projects/
├── LLM/                              # Drawing with LLM — Qwen-7B QLoRA fine-tuning
├── Dual Model Job Recommendation System/   # Hybrid TF-IDF + SVD recommender
├── AML project/                      # Applied ML: Credit Card Default + Internet Usage
├── Big Data/                         # Airbnb pricing analytics with Apache Spark
├── Cloud-Based Image Sharing Platform (Azure, Docker, Serverless)/
├── Time Series/                      # Ferrari F1 pit-stop forecasting in R
└── supply chain/                     # Supply chain analytics & BI dashboards
```

---

## Projects Overview

### 01 · Drawing with LLM
**Folder:** `LLM/`
Fine-tuned a Qwen-7B large language model using QLoRA on 10,000 SVG–prompt pairs to generate structured vector graphics from natural language descriptions. Achieved improved shape alignment over zero-shot baseline using 4-bit quantization on a single A100 GPU.

**Stack:** Python · Qwen-7B · QLoRA · Hugging Face · Prompt Engineering

---

### 02 · Dual Model Job Recommendation System
**Folder:** `Dual Model Job Recommendation System/`
Hybrid recommendation engine combining TF-IDF cosine similarity (content-based) and SVD collaborative filtering on 1,000+ applicant profiles. Dynamic weighting solves the cold-start problem. Achieved **+17% precision, +14% recall, +19% F1** over TF-IDF baseline.

**Stack:** Python · Scikit-learn · TF-IDF · SVD · NLP

---

### 03 · Applied ML (Credit Card Default + Internet Usage)
**Folder:** `AML project/`
Two applied classification projects:
- **Credit Card Default Prediction:** PCA on 23 features → 8 PCs (96.3% variance retained), **0.88 AUC**, 41% faster training on 30K+ records.
- **Problematic Internet Usage:** Multi-class classifiers with K-Means feature engineering. **98.7% accuracy** on 1,500+ adolescent records.

**Stack:** Python · Scikit-learn · PCA · SVD · Logistic Regression · K-Means · Decision Trees · SMOTE

---

### 04 · Pricing & Regional Trends in Airbnb Markets
**Folder:** `Big Data/`
Scalable Apache Spark ETL pipeline on millions of Airbnb listing records across U.S. cities. Log-log regression for price elasticity — location explains 11–25% of price variability. **80% runtime reduction** scaling from single-node to 4-worker Spark cluster.

**Stack:** Python · Apache Spark · SQL · Regression · Big Data

---

### 05 · Cloud-Based Image Sharing Platform
**Folder:** `Cloud-Based Image Sharing Platform (Azure, Docker, Serverless)/`
Production-grade Azure-native image sharing platform with event-driven ML pipeline. Cosmos DB change-feed triggers auto-classify uploaded images. Containerized with Docker on Azure App Service with Azure Key Vault secrets management.

**Stack:** Python · Azure · Docker · Serverless Functions · Cosmos DB · Blob Storage · MLOps

---

### 06 · Ferrari F1 Pit-Stop & Lap-Time Forecasting
**Folder:** `Time Series/`
Time-series framework in R modeling Ferrari F1 pit-stop durations and lap times. SARIMA models selected via auto.arima (AIC/BIC), validated with k-fold cross-validation and Ljung-Box residual diagnostics. Evaluated via RMSE and MAE.

**Stack:** R · SARIMA · ACF/PACF · auto.arima · Time-Series Forecasting

---

### 07 · Supply Chain Sales Analytics & Forecasting
**Folder:** `supply chain/`
SQL-driven analysis of 1M+ sales records surfacing a 15% revenue decline across 5 regions. Built 10+ Tableau dashboards for operations leadership. Improved forecast accuracy by **+20%** by integrating historical trend analysis into supply chain planning models.

**Stack:** SQL · Python · Tableau · Power BI · Forecasting

---

## Skills Demonstrated Across Projects

| Domain | Tools |
|--------|-------|
| Machine Learning | Scikit-learn · TensorFlow · Hugging Face · SVM · PCA · K-Means |
| NLP & LLMs | TF-IDF · SVD · QLoRA · Qwen-7B · Prompt Engineering |
| Big Data | Apache Spark · SQL · ETL Pipelines |
| Cloud & MLOps | Azure · Docker · Serverless · Cosmos DB · Key Vault |
| Time-Series | R · ARIMA · SARIMA · ACF/PACF |
| BI & Visualization | Tableau · Power BI |

---

*For full project descriptions and live demos, visit the [Portfolio](https://coderx-com.github.io/Portfolio).*
