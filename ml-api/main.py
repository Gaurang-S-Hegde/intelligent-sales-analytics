from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="Intelligent Sales Analytics API",
    description="Customer churn prediction API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained ML files
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")


class CustomerData(BaseModel):
    TotalSpent: float
    TotalOrders: int
    TotalQuantity: int
    AverageOrderValue: float
    CustomerLifetime: int
    Recency: int
    Frequency: int


@app.get("/")
def home():
    return {
        "message": "Intelligent Sales Analytics API is running",
        "model": "Logistic Regression",
        "status": "success"
    }


@app.post("/predict")
def predict_churn(customer: CustomerData):

    data = np.array([[
        customer.TotalSpent,
        customer.TotalOrders,
        customer.TotalQuantity,
        customer.AverageOrderValue,
        customer.CustomerLifetime,
        customer.Recency,
        customer.Frequency
    ]])

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)[0]

    probability = model.predict_proba(scaled_data)[0][1]

    if probability >= 0.70:
        risk_level = "HIGH"
    elif probability >= 0.40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(float(probability), 4),
        "risk_level": risk_level
    }