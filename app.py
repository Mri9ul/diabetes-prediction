import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺"
)

st.title("🩺 Diabetes Prediction")
st.warning(
    "This app is for educational purposes only and should not be used for real medical diagnosis."
)

st.write("Enter the details below to check whether a person is diabetic or not.")

# Input fields
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Prediction
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 0:
        st.success("The person is NOT diabetic")
    else:
        st.error("The person is diabetic")