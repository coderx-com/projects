import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 VaR & Expected Shortfall")

@st.cache_data
def load_data():
    df = pd.read_csv("dashboard_data/plot_df.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

ticker = st.selectbox("Select Ticker", sorted(df["ticker"].unique()))
window = st.selectbox("Rolling Window (days)", [20, 60, 120])
confidence = st.selectbox("Confidence Level", [0.95, 0.99])

ticker_df = df[df["ticker"] == ticker].copy()
ticker_df["returns"] = ticker_df["close"].pct_change()
returns = ticker_df["returns"].dropna()

alpha = (1 - confidence) * 100
VaR = np.percentile(returns, alpha)
ES = returns[returns <= VaR].mean()

st.metric("Value at Risk (VaR)", f"{VaR:.2%}")
st.metric("Expected Shortfall (ES)", f"{ES:.2%}")

fig, ax = plt.subplots(figsize=(10,4))
ax.hist(returns, bins=50, alpha=0.7)
ax.axvline(VaR, color="red", linestyle="--", label="VaR")
ax.set_title("Return Distribution")
ax.legend()

st.pyplot(fig)

st.markdown("""
**Interpretation**  
VaR estimates the worst expected loss at the chosen confidence level,  
while Expected Shortfall captures the average loss beyond VaR.
""")

