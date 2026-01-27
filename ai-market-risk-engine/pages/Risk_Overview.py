import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📈 Risk Overview")

@st.cache_data
def load_data():
    df = pd.read_csv("dashboard_data/plot_df.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

ticker = st.selectbox("Select Ticker", sorted(df["ticker"].unique()))
ticker_df = df[df["ticker"] == ticker]

fig, ax = plt.subplots(figsize=(12,4))

ax.plot(
    ticker_df["date"],
    ticker_df["close"],
    label="Price",
    linewidth=2
)

ax.scatter(
    ticker_df[ticker_df["risk_label"] == 1]["date"],
    ticker_df[ticker_df["risk_label"] == 1]["close"],
    color="red",
    s=20,
    label="High Risk Regime"
)

ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()

st.pyplot(fig)

st.markdown("""
**Interpretation**  
Red markers indicate periods where the model detected a high-risk volatility regime.
""")

