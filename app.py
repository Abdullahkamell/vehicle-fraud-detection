import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="FraudShield AI", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9233/9233515.png", width=100)
    st.title("FraudShield AI")
    st.info("An AI-powered system to detect fraudulent vehicle insurance claims using XGBoost.")
    st.markdown("---")
    st.write("👤 **Developed by:** Abdullah")

st.title("🛡️ Vehicle Insurance Fraud Detection System")
st.write("Enter the claim details below to analyze the probability of fraud.")

tab1, tab2, tab3 = st.tabs(["👤 Insured Details", "🚗 Incident Info", "💰 Claim Details"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        insured_age = st.slider("Insured Age", 18, 100, 35)
        insured_sex = st.radio("Insured Sex", [0, 1], format_func=lambda x: "Male" if x==1 else "Female", horizontal=True)
        policy_state = st.selectbox("Policy State", [0, 1, 2])
    with col2:
        insured_education_level = st.select_slider("Education Level", options=[0, 1, 2, 3, 4, 5, 6])
        insured_occupation = st.number_input("Occupation ID (0-13)", 0, 13, 5)
        insured_hobbies = st.number_input("Hobbies ID (0-19)", 0, 19, 10)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        incident_type = st.selectbox("Incident Type", [0, 1, 2, 3])
        collision_type = st.selectbox("Collision Type", [0, 1, 2, 3])
        incident_severity = st.select_slider("Incident Severity", options=[0, 1, 2, 3])
        incident_hour = st.slider("Incident Hour", 0, 23, 12)
    with col2:
        authorities_contacted = st.selectbox("Authorities Contacted", [0, 1, 2, 3, 4])
        incident_state = st.number_input("Incident State (0-6)", 0, 6, 2)
        incident_city = st.number_input("Incident City (0-6)", 0, 6, 3)
        vehicles_involved = st.number_input("Vehicles Involved", 1, 4, 1)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        policy_deductible = st.number_input("Policy Deductible", 500, 2000, 1000)
        policy_annual_premium = st.number_input("Annual Premium", 500.0, 2500.0, 1200.0)
        police_report = st.selectbox("Police Report Available", [0, 1])
    with col2:
        claim_amount = st.number_input("Claim Amount", 0.0, 10000.0, 5000.0)
        total_claim = st.number_input("Total Claim Amount", 0.0, 100000.0, 55000.0)
        incident_month = st.number_input("Month", 1, 12, 1)
        incident_day = st.number_input("Day", 1, 31, 15)
        witnesses = st.number_input("Witnesses", 0, 3, 0)
        bodily_injuries = st.number_input("Bodily Injuries", 0, 2, 0)

st.markdown("---")

if st.button("🚀 Analyze Claim"):
    data = {
        "policy_state": policy_state, "policy_deductible": policy_deductible,
        "policy_annual_premium": policy_annual_premium, "insured_age": insured_age,
        "insured_sex": insured_sex, "insured_education_level": insured_education_level,
        "insured_occupation": insured_occupation, "insured_hobbies": insured_hobbies,
        "incident_type": incident_type, "collision_type": collision_type,
        "incident_severity": incident_severity, "authorities_contacted": authorities_contacted,
        "incident_state": incident_state, "incident_city": incident_city,
        "incident_hour_of_the_day": incident_hour, "number_of_vehicles_involved": vehicles_involved,
        "bodily_injuries": bodily_injuries, "witnesses": witnesses,
        "police_report_available": police_report, "claim_amount": claim_amount,
        "total_claim_amount": total_claim, "incident_month": incident_month,
        "incident_day": incident_day
    }
    
    try:
        with st.spinner('Analyzing data...'):
            response = requests.post("http://127.0.0.1:8000/predict", json=data)
            result = response.json()
        
        prob = result["probability"]
        
        if result["prediction"] == 1:
            st.error(f"### 🚩 High Probability of Fraud Detected!")
            st.metric("Fraud Confidence", f"{prob:.2%}")
        else:
            st.success(f"### ✅ Claim Appears to be Legitimate")
            st.metric("Risk Level", f"{prob:.2%}")
            st.balloons()
            
    except Exception as e:
        st.error("❌ Connection Failed. Please make sure FastAPI server is running.")