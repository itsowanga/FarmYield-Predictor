import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Load dataset
columns = ['crop', 'rainfall', 'pH', 'month']

try:
    data = pd.read_csv('input.txt', names=columns)
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
x = data.drop(['crop', 'month'], axis=1)

# Load the model
model_file = 'model.joblib'
model = joblib.load(model_file)
# Predict the target
y_pred = model.predict(x)
# Output predictions

for i, prediction in enumerate(y_pred):
    with open('results.txt', 'a') as f:
        f.write(f"Expected = {prediction:.1f} tons/ha\n")

print("Predictions saved to results.txt")
f.close()
