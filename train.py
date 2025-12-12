import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Load dataset
try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()
except pd.errors.EmptyDataError:
    print("No data found. Please check the file.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Separate features from the target
x = data.drop(['crop', 'yield_tons_per_ha'], axis=1)
# Extract the target
y = data['yield_tons_per_ha']
# Split the model training with 80/20 split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=33)

model = LinearRegression()

model.fit(x_train, y_train)
# Predict the target 
y_pred = model.predict(x_test)
model_file = 'model.joblib'
joblib.dump(model, model_file)
print(f"Model saved successfully to {model_file}")





