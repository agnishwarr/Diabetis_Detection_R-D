import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model/rf_diabetes_model.pkl")

st.title("🧠 Diabetes Risk Prediction ")
st.markdown("Predict whether a person has diabetes based on health and behavioral factors.")

st.sidebar.header("Input Health Indicators")

# All features based on dataset
def get_user_input():
    HighBP = st.sidebar.selectbox("High Blood Pressure (1=Yes, 0=No)", [0, 1])
    HighChol = st.sidebar.selectbox("High Cholesterol (1=Yes, 0=No)", [0, 1])
    CholCheck = st.sidebar.selectbox("Cholesterol Check (1=Yes, 0=No)", [0, 1])
    BMI = st.sidebar.slider("BMI", 10, 70, 25)
    Smoker = st.sidebar.selectbox("Smoker (1=Yes, 0=No)", [0, 1])
    Stroke = st.sidebar.selectbox("History of Stroke (1=Yes, 0=No)", [0, 1])
    HeartDiseaseorAttack = st.sidebar.selectbox("Heart Disease or Attack (1=Yes, 0=No)", [0, 1])
    PhysActivity = st.sidebar.selectbox("Physical Activity (1=Yes, 0=No)", [0, 1])
    Fruits = st.sidebar.selectbox("Fruits Intake (1=Yes, 0=No)", [0, 1])
    Veggies = st.sidebar.selectbox("Vegetable Intake (1=Yes, 0=No)", [0, 1])
    HvyAlcoholConsump = st.sidebar.selectbox("Heavy Alcohol Consumption (1=Yes, 0=No)", [0, 1])
    AnyHealthcare = st.sidebar.selectbox("Access to Healthcare (1=Yes, 0=No)", [0, 1])
    NoDocbcCost = st.sidebar.selectbox("Doctor Unavailable Due to Cost (1=Yes, 0=No)", [0, 1])
    GenHlth = st.sidebar.slider("General Health (1=Excellent, 5=Poor)", 1, 5, 3)
    MentHlth = st.sidebar.slider("Mental Health (Days unwell, past month)", 0, 30, 5)
    PhysHlth = st.sidebar.slider("Physical Health (Days unwell, past month)", 0, 30, 5)
    DiffWalk = st.sidebar.selectbox("Difficulty Walking (1=Yes, 0=No)", [0, 1])
    Sex = st.sidebar.selectbox("Sex (1=Male, 0=Female)", [0, 1])
    Age = st.sidebar.slider("Age (Category: 1 to 13)", 1, 13, 5)
    #Education = st.sidebar.slider("Education Level (1=Low to 6=High)", 1, 6, 4)
    #Income = st.sidebar.slider("Income Level (1=Low to 8=High)", 1, 8, 4)

    return np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity,
                      Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth,
                      PhysHlth, DiffWalk, Sex, Age]])

input_data = get_user_input()

if st.button("Predict Diabetes Risk"):
    prediction = model.predict(input_data)
    result = "Diabetic (Pre or Full)" if prediction[0] == 1 else "Not Diabetic"
    st.success(f"🔎 Prediction: **{result}**")
