# Retail Sales Forecasting Using Machine Learning

## Project Overview

This project predicts future retail sales using machine learning models and time-series feature engineering. The system helps businesses forecast sales and make better inventory and promotion decisions.

## Dataset

Walmart Retail Sales Dataset including store information, promotions, holidays, fuel price, CPI, and unemployment data.

## Machine Learning Workflow

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Lag Features & Rolling Mean
* Model Training
* Model Comparison
* Model Evaluation
* Feature Importance
* Sales Forecasting
* Streamlit Dashboard Deployment

## Models Used

| Model             | R2 Score |
| ----------------- | -------- |
| Linear Regression | 0.17     |
| Gradient Boosting | 0.77     |
| Random Forest     | 0.81     |

Random Forest performed best and was selected as the final model.

## Key Insights

* Promotions significantly increase sales
* Holiday weeks have higher sales
* Previous week sales strongly influence future sales
* Fuel price and CPI impact sales trends

## Streamlit Dashboard

The Streamlit app allows users to input store and date information to predict future sales.

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib
