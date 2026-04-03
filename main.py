from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

with open("xgboost_fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

class ClaimData(BaseModel):
    policy_state: int
    policy_deductible: int
    policy_annual_premium: float
    insured_age: int
    insured_sex: int
    insured_education_level: int
    insured_occupation: int
    insured_hobbies: int
    incident_type: int
    collision_type: int
    incident_severity: int
    authorities_contacted: int
    incident_state: int
    incident_city: int
    incident_hour_of_the_day: int
    number_of_vehicles_involved: int
    bodily_injuries: int
    witnesses: int
    police_report_available: int
    claim_amount: float
    total_claim_amount: float
    incident_month: int
    incident_day: int

@app.post("/predict")
def predict_fraud(data: ClaimData):
    input_dict = data.model_dump()
    input_df = pd.DataFrame([input_dict])
    
    input_scaled = scaler.transform(input_df)
    
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]
    
    return {
        "prediction": int(prediction[0]),
        "probability": float(probability)
    }