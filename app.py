import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib

# Load trained model
model = load_model("heart_disease_model.h5")

# Load the scaler (optional if you saved it)
try:
    scaler = joblib.load("scaler.pkl")
except:
    scaler = None

# App title
st.title("🫀 Heart Disease Prediction App")
st.write("Enter your health details below to check the risk of heart disease.")

# Input fields for features
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ("Male", "Female"))
cp = st.selectbox("Chest Pain Type", (0, 1, 2, 3))
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", (0, 1))
restecg = st.selectbox("Rest ECG", (0, 1, 2))
thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina", (0, 1))
oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=6.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of ST Segment", (0, 1, 2))
ca = st.selectbox("Number of Major Vessels (0-3)", (0, 1, 2, 3))
thall = st.selectbox("Thalassemia", (0, 1, 2, 3))

# Convert input to numpy array
input_data = np.array([[age, 1 if sex == "Male" else 0, cp, trestbps, chol, fbs, restecg, thalach, 
                        exang, oldpeak, slope, ca, thall]])

# Scale the data if scaler exists
if scaler:
    input_data = scaler.transform(input_data)

# Predict button
if st.button("Predict Risk"):
    prediction = model.predict(input_data)
    result = "High Risk of Heart Disease" if prediction > 0.5 else "Low Risk of Heart Disease"

    st.subheader("Prediction Result:")
    if prediction > 0.5:
        st.error(f"⚠️ {result} ({prediction[0][0]*100:.2f}%)")
    else:
        st.success(f"✅ {result} ({(1-prediction[0][0])*100:.2f}%)")

# Footer
st.markdown("---")
st.caption("This tool is for educational purposes and should not replace professional medical advice.")
