import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/churn_model.pkl")

st.title("Customer Churn Prediction System")
st.write("Enter customer details to predict churn risk")

# -------- USER INPUTS -------- #

tenure = st.slider("Tenure (months)", 0, 72, 12)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=20.0,
    max_value=120.0,
    value=70.0
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

# -------- RECREATE TRAINING FEATURE STRUCTURE -------- #

df = pd.read_csv("data/Telcom-Customer-Churn.csv")

df.drop("customerID", axis=1, inplace=True)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

df["tenure_group"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 72],
    labels=["0-1yr", "1-2yr", "2-4yr", "4-6yr"]
)

df["avg_monthly_spend"] = df["TotalCharges"] / (df["tenure"] + 1)

df = pd.get_dummies(df, drop_first=True)

feature_columns = df.drop("Churn", axis=1).columns

# -------- PREDICTION -------- #

if st.button("Predict Churn"):

    # create empty row with correct features
    input_df = pd.DataFrame(columns=feature_columns)
    input_df.loc[0] = 0

    # fill user inputs
    input_df["tenure"] = tenure
    input_df["MonthlyCharges"] = monthly_charges

    # contract encoding
    if contract == "One year":
        input_df["Contract_One year"] = 1
    elif contract == "Two year":
        input_df["Contract_Two year"] = 1

    # internet service encoding
    if internet_service == "Fiber optic":
        input_df["InternetService_Fiber optic"] = 1
    elif internet_service == "No":
        input_df["InternetService_No"] = 1

    # predict
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    st.write("Churn Probability:", round(probability, 2))

    if probability > 0.7:
        st.error("High Risk Customer")
    elif probability > 0.3:
        st.warning("Medium Risk Customer")
    else:
        st.success("Low Risk Customer")