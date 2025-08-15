# src/train.py
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("data/data.csv")
X = df.drop(columns=["price"])
y = df["price"]

# Build pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

# Train model
pipeline.fit(X, y)

# Save model
joblib.dump(pipeline, "model/model.pkl")
print("Model saved to model/model.pkl")
