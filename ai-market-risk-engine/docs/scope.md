## Project Scope

Domain: Equity Market Risk Analysis  
Sector: Technology  

Companies:
- AAPL
- MSFT
- AMZN
- NVDA
- GOOGL

Goal:
Predict whether a stock will enter a high-risk period in the next 30 days
using historical market data and unstructured financial documents.

## Problem Statement

Market participants often react to risk only after volatility spikes.
This project aims to identify early warning signals by predicting
whether a stock is likely to enter a high-risk volatility regime
within the next 30 days.

## Risk Definition (Initial)

A high-risk period is defined as a future window where realized
volatility significantly exceeds the stock’s historical norm.
The exact labeling rule will be defined after exploratory analysis.

# AI Market Risk Engine

An end-to-end ML + GenAI system that predicts upcoming high-risk periods
for technology stocks by combining market data with financial filings.
The system provides both risk forecasts and explainable, evidence-backed insights.

## Risk Label Definition

Task:
Binary classification to predict whether a stock will enter a high-risk
volatility regime in the next 30 trading days.

Volatility Measure:
30-day rolling standard deviation of log returns.

Label Rule:
label_t = 1 if future 30-day realized volatility exceeds the stock’s
historical 75th percentile volatility; else 0.

Prediction Horizon:
30 trading days.

Data Splits:
Train: 2019–2022  
Validation: 2023  
Test: 2024–present

Rationale:
This approach captures regime shifts in market risk while avoiding
look-ahead bias and maintaining interpretability.
