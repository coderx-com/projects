import streamlit as st
import pandas as pd
import numpy as np
import shap
import json
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🧠 Factor Analysis (SHAP)")

@st.cache_data
def load_data():
    test_df = pd.read_csv("dashboard_data/test_df.csv")
    X_test = np.load("dashboard_data/X_test.npy")
    shap_values = np.load("dashboard_data/shap_values.npy")
    with open("dashboard_data/features.json", "r") as f:
        features = json.load(f)
    return test_df, X_test, shap_values, features

test_df, X_test, shap_values, FEATURES = load_data()

ticker = st.selectbox("Select Ticker", sorted(test_df["ticker"].unique()))
ticker_test_df = test_df[test_df["ticker"] == ticker]

idx = st.selectbox(
    "Select observation (row index)",
    ticker_test_df.index
)

st.subheader("Why the model predicted this risk")

# Use class 1 SHAP values (risk = 1)
shap_class_1 = shap_values[:, :, 1]

fig = plt.figure()
shap.plots.waterfall(
    shap.Explanation(
        values=shap_class_1[idx],
        base_values=0,
        feature_names=FEATURES
    ),
    show=False
)

st.pyplot(fig)

st.markdown("""
**Explanation**  
The waterfall plot shows how each feature contributed to increasing or decreasing
the predicted risk for this specific day.
""")

