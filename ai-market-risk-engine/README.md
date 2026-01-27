# Market Risk Regime Prediction using Machine Learning

## Overview
This project builds a time-aware machine learning system to predict upcoming high-volatility market regimes for large-cap technology stocks.  
The objective is not price prediction, but **risk regime identification**, enabling proactive risk management.

## Data Pipeline
- Market data sourced using `yfinance`
- Stored and processed using **Google Cloud Platform**
  - Google Cloud Storage (raw + processed Parquet)
  - BigQuery (analytical tables)
- End-to-end pipeline built in Python using Pandas and BigQuery APIs

## Feature Engineering
Key features were designed to capture market risk dynamics:
- Rolling volatility (10 / 20 / 30 days)
- Momentum indicators
- Volume anomaly (z-score)
- Drawdown from recent peaks

These features explicitly model volatility persistence and stress conditions.

## Modeling Approach
- Binary classification: Will the stock enter a high-volatility regime in the next 30 trading days?
- Time-based train / validation / test split (no leakage)
- Models:
  - Logistic Regression (baseline)
  - Random Forest (final model)

## Performance
- ROC-AUC: ~0.94 (out-of-sample)
- Recall: ~0.96 (risk detection)
- Random Forest selected for strong non-linear modeling

## Explainability
- SHAP global feature importance confirms volatility dominance
- Local SHAP waterfall plots explain individual risk predictions
- Interaction plots reveal volatility persistence across horizons

## Key Insights
- Volatility persistence across multiple windows is the strongest risk signal
- Risk emerges through regime transitions, not single-day spikes
- Explainability validates financial intuition behind model decisions

## Technologies
Python, Pandas, Scikit-learn, SHAP, Google Cloud Storage, BigQuery, Matplotlib

## Use Cases
- Market risk monitoring
- Portfolio risk overlays
- Quantitative research
