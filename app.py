import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model_logistic.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Dashboard Student Dropout", layout="wide")

st.title("Prediksi Student Dropout")
st.markdown("Sistem prediksi risiko mahasiswa dropout menggunakan Machine Learning")

st.sidebar.header("Input Data Mahasiswa")

credited_2nd = st.sidebar.number_input("2nd Sem Credited Units", 0, 30, 5)
approved_2nd = st.sidebar.number_input("2nd Sem Approved Units", 0, 20, 5)
enrolled_2nd = st.sidebar.number_input("2nd Sem Enrolled Units", 0, 23, 5)
approved_1st = st.sidebar.number_input("1st Sem Approved Units", 0, 26, 5)
enrolled_1st = st.sidebar.number_input("1st Sem Enrolled Units", 0, 30, 5)

grade_2nd = st.sidebar.slider("2nd Sem Grade", 0.0, 20.0, 10.0)
age = st.sidebar.slider("Age at Enrollment", 16, 70, 20)

mother_occ = st.sidebar.number_input("Mother's Occupation (Encoded)", 0, 20, 1)

tuition = st.sidebar.selectbox(
    "Tuition Fees Up To Date",[0, 1],format_func=lambda x: "Yes" if x == 1 else "No"
)

course_code = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)"
}
course = st.sidebar.selectbox(
    "Course",
    options=list(course_code.keys()),
    format_func=lambda x: f"{x} - {course_code[x]}"
)


if st.sidebar.button("🔍 Prediksi Status"):

    input_data = np.array([[ 
        approved_2nd,
        enrolled_2nd,
        approved_1st,
        tuition,
        grade_2nd,
        credited_2nd,
        age,
        mother_occ,
        enrolled_1st,
        course
    ]])

    input_scaled = scaler.transform(input_data)

    predict = model.predict(input_scaled)
    proba = model.predict_proba(input_scaled)

    status_map = {
        0: "Dropout",
        1: "Enrolled",
        2: "Graduate"
    }

    predicted_status = status_map[predict[0]]

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Prediksi Status", predicted_status)

    with col2:
        st.metric("Probabilitas Dropout", f"{proba[0][0]*100:.2f}%") #persentase baris pertama kelas dropout

    st.subheader("Distribusi Probabilitas")
    prob_df = pd.DataFrame({
        "Status": ["Dropout", "Enrolled", "Graduate"],
        "Probability": proba[0]
    })

    st.bar_chart(prob_df.set_index("Status"))
    if proba[0][0] > 0.6:
        st.error("🚨 Risiko Dropout Tinggi")
    elif proba[0][0] > 0.4:
        st.warning("⚠️ Risiko Dropout Sedang")
    else:
        st.success("✅ Risiko Dropout Rendah")