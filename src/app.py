# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("model/model.pkl")

class HouseFeatures(BaseModel):
    size_sqft: float
    bedrooms: int
    age_years: float

app = FastAPI()

@app.post("/predict")
def predict(data: HouseFeatures):
    features = np.array([[data.size_sqft, data.bedrooms, data.age_years]])
    prediction = model.predict(features)[0]
    return {"predicted_price": float(prediction), "message": features.tolist()}
