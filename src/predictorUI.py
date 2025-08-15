import streamlit as st
import requests

st.title("📊 AI Price Predictor")

# Adjust these to match your FastAPI model's features
feature1 = st.number_input("Size in Sqrt", min_value=0.0, value=5.0)
feature2 = st.number_input("Bedroom", min_value=0.0, value=5.0)
feature3 = st.number_input("Age years", min_value=0.0, value=5.0)

if st.button("Predict"):
    payload = {
        "size_sqft": feature1,
        "bedrooms": feature2,
        "age_years": feature3
    }
    
    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            print(result)
            
            
            st.success(f"Predicted Value: {result['predicted_price']:.2f}")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to FastAPI server. Is it running?")
