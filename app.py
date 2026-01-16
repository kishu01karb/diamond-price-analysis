# STEP 9: MAKE PREDICTIONS ON NEW DIAMONDS

import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# -------------------------------------------------
# Load data & train models (cached)
# -------------------------------------------------
@st.cache_resource
def train_models():
    # Load dataset (must be available in repo or via URL)
    df = pd.read_csv("https://github.com/kishu01karb/diamond-price-analysis/blob/main/diamonds.csv")

    # Encode categorical variables
    le_cut = LabelEncoder()
    le_color = LabelEncoder()
    le_clarity = LabelEncoder()

    df["cut"] = le_cut.fit_transform(df["cut"])
    df["color"] = le_color.fit_transform(df["color"])
    df["clarity"] = le_clarity.fit_transform(df["clarity"])

    # Features & target
    X = df[["carat", "cut", "color", "clarity", "depth", "table", "x", "y", "z"]]
    y = df["price"]

    # Train models
    lr_model = LinearRegression()
    rf_model = RandomForestRegressor(
        n_estimators=50,
        random_state=42,
        n_jobs=-1
    )

    lr_model.fit(X, y)
    rf_model.fit(X, y)

    label_encoders = {
        "cut": le_cut,
        "color": le_color,
        "clarity": le_clarity
    }

    return lr_model, rf_model, label_encoders


# Load trained models
lr_model, rf_model, label_encoder = train_models()

# -------------------------------------------------
# Prediction function
# -------------------------------------------------
def predict_diamond_price(carat, cut, color, clarity, depth, table, x, y, z):
    """
    Predict the price of a diamond based on its characteristics
    """

    # Encode categorical inputs
    cut_encoded = label_encoder["cut"].transform([cut])[0]
    color_encoded = label_encoder["color"].transform([color])[0]
    clarity_encoded = label_encoder["clarity"].transform([clarity])[0]

    # Feature array
    features = np.array([[
        carat,
        cut_encoded,
        color_encoded,
        clarity_encoded,
        depth,
        table,
        x,
        y,
        z
    ]])

    # Predictions
    price_lr = lr_model.predict(features)[0]
    price_rf = rf_model.predict(features)[0]
    avg_price = (price_lr + price_rf) / 2

    # Display results
    st.subheader("🔍 Diamond Characteristics")
    st.write(
        f"Carat: {carat}, Cut: {cut}, Color: {color}, "
        f"Clarity: {clarity}, Depth: {depth}, Table: {table}, "
        f"X: {x}, Y: {y}, Z: {z}"
    )

    st.subheader("💰 Predicted Prices")
    st.write(f"Linear Regression: **$ {price_lr:.2f}**")
    st.write(f"Random Forest: **$ {price_rf:.2f}**")
    st.success(f"Average Estimated Price: **$ {avg_price:.2f}**")

    return avg_price


# -------------------------------------------------
# Streamlit UI
# -------------------------------------------------
st.title("💎 Diamond Price Predictor")

carat = st.number_input("Carat", min_value=0.01, step=0.01)
cut = st.selectbox("Cut", label_encoder["cut"].classes_)
color = st.selectbox("Color", label_encoder["color"].classes_)
clarity = st.selectbox("Clarity", label_encoder["clarity"].classes_)
depth = st.number_input("Depth", min_value=0.0, step=0.1)
table = st.number_input("Table", min_value=0.0, step=0.1)
x = st.number_input("X (length in mm)", min_value=0.0, step=0.01)
y = st.number_input("Y (length in mm)", min_value=0.0, step=0.01)
z = st.number_input("Z (length in mm)", min_value=0.0, step=0.01)

if st.button("Predict Price"):
    predict_diamond_price(carat, cut, color, clarity, depth, table, x, y, z)
