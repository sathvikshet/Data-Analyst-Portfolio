import streamlit as st
import pandas as pd
import joblib
import os

# Paths
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, '..', 'models', 'sales_forecast_model.pkl')
columns_path = os.path.join(base_path, '..', 'models', 'model_columns.pkl')

# Load model and columns
model = joblib.load(model_path)
model_columns = joblib.load(columns_path)

st.title("Retail Sales Forecasting Dashboard")

store = st.number_input("Store", 1, 50, 1)
month = st.slider("Month", 1, 12, 6)
week = st.slider("Week", 1, 52, 20)

if st.button("Predict Sales"):
    input_data = pd.DataFrame([[store, month, week]], columns=['Store','Month','Week'])
    
    # Add missing columns
    for col in model_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[model_columns]

    prediction = model.predict(input_data)
    st.success(f"Predicted Sales: {prediction[0]:,.2f}")