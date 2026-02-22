import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model & scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Student Dropout Prediction", layout="wide")

st.title("Student Dropout Prediction Dashboard")
st.markdown("Prototype sistem prediksi risiko mahasiswa dropout menggunakan Machine Learning")

st.sidebar.header("Input Data Mahasiswa")

age = st.sidebar.slider("Umur", 17, 40, 20)
gpa = st.sidebar.slider("GPA", 0.0, 4.0, 2.5)
attendance = st.sidebar.slider("Attendance (%)", 0, 100, 75)
credits = st.sidebar.slider("Credits Approved", 0, 60, 30)

gender = st.sidebar.selectbox("Gender", ["Perempuan", "Laki-laki"])
scholarship = st.sidebar.selectbox("Scholarship Holder", ["Yes", "No"])

gender = 1 if gender == "Laki-laki" else 0
scholarship = 1 if scholarship == "Yes" else 0

if st.sidebar.button("🔍 Prediksi Status"):

    input_data = np.array([[age, gpa, attendance, credits, gender, scholarship]])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)
    proba = model.predict_proba(input_scaled)

    status_map = {
        0: "Dropout",
        1: "Enrolled",
        2: "Graduate"
    }

    predicted_status = status_map[prediction[0]]

    # =============================
    # OUTPUT
    # =============================
    st.subheader("📊 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Predicted Status", predicted_status)

    with col2:
        st.metric("Dropout Probability", f"{proba[0][0]*100:.2f}%")

    st.subheader("📈 Probability Distribution")

    prob_df = pd.DataFrame({
        "Status": ["Dropout", "Enrolled", "Graduate"],
        "Probability": proba[0]
    })

    st.bar_chart(prob_df.set_index("Status"))

    # Risk Alert
    if proba[0][0] > 0.6:
        st.error("⚠️ High Risk of Dropout!")
    elif proba[0][0] > 0.4:
        st.warning("⚠️ Medium Risk")
    else:
        st.success("✅ Low Risk")