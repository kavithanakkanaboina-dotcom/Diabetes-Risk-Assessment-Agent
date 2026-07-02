import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")

st.title("🩺 Diabetes Prediction System")
st.write("Enter the patient details below:")

# User Inputs
Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
Glucose = st.number_input("Glucose", min_value=0, value=120)
BloodPressure = st.number_input("Blood Pressure", min_value=0, value=70)
SkinThickness = st.number_input("Skin Thickness", min_value=0, value=20)
Insulin = st.number_input("Insulin", min_value=0, value=79)
BMI = st.number_input("BMI", min_value=0.0, value=25.0)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.5)
Age = st.number_input("Age", min_value=1, value=30)

# Prediction
if st.button("Predict"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure,
                            SkinThickness, Insulin, BMI,
                            DiabetesPedigreeFunction, Age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Diabetes")
        st.write("### Recommendations")
        st.write("- Consult a doctor.")
        st.write("- Follow a healthy diet.")
        st.write("- Exercise regularly.")
        st.write("- Monitor your blood sugar levels.")
    else:
        st.success("✅ Low Risk of Diabetes")
        st.write("### Recommendations")
        st.write("- Maintain a healthy lifestyle.")
        st.write("- Eat a balanced diet.")
        st.write("- Exercise regularly.")
        st.write("- Get regular health checkups.")
