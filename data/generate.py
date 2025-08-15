import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Number of samples
n = 300

# Features
size_sqft = np.random.normal(1200, 300, n)        # house size
bedrooms = np.random.randint(1, 5, n)            # number of bedrooms
age_years = np.random.randint(0, 30, n)          # age of the house

# Target variable (price)
price = 25000 + 150*size_sqft + 18000*bedrooms - 700*age_years + np.random.normal(0, 20000, n)

# Create DataFrame
df = pd.DataFrame({
    "size_sqft": size_sqft.round(1),
    "bedrooms": bedrooms,
    "age_years": age_years,
    "price": price.round(0).astype(int)
})

# Save to CSV
df.to_csv("data.csv", index=False)
print("Dataset saved to data/data.csv")
