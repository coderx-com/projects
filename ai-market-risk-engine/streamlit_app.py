import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

st.set_page_config(
    page_title="Market Risk Regime Explorer",
    layout="wide"
)

st.title("Market Risk Regime Explorer")
st.caption("Interactive exploration of predicted market risk regimes with explainable ML")

# ---------- Load data ----------
@st.cache_data
def load_data():
    plot_df = pd.read_csv("dashboard_data/plot_df.csv")
    plot_df["date"] = pd.to_datetime(plot_df["date"])

    test_df = pd.read_csv("dashboard_data/test_df.csv")

    X_test = np.load("dashboard_data/X_test.npy")
    shap_values = np.load("dashboard_data/shap_values.npy")

    with open("dashboard_data/features.json", "r") as f:
        features = json.load(f)

    return plot_df, test_df, X_test, shap_values, features


plot_df, test_df, X_test, shap_values, FEATURES = load_data()

# ---------- Sidebar ----------
st.sidebar.header("Controls")

ticker = st.sidebar.selectbox(
    "Select stock",
    sorted(plot_df["ticker"].unique())
)

st.write(f"### {ticker} — Price with Predicted Risk Periods")
