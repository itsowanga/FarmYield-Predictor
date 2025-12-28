import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Load dataset
columns = ['crop', 'rainfall', 'ph']

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
x = data.drop(['crop'], axis=1)

# Load the model
model_file = 'model.joblib'
model = joblib.load(model_file)
# Predict the target
y_pred = model.predict(x)

# Create results dataframe
results_data = []

for i, prediction in enumerate(y_pred):
    rainfall = x.iloc[i]['rainfall']
    crop = data.iloc[i]['crop']
    
    # Yield risk
    if prediction < 3.0:
        yield_status = "LOW YIELD RISK"
    else:
        yield_status = "Good yield expected"
    
    # Rainfall risk
    if rainfall < 400:
        rainfall_status = "Low rainfall - Consider drought-resistant seed"
    else:
        rainfall_status = "Rainfall is adequate"
    
    # Planting window
    planting_window = "October - November"
    
    results_data.append({
        'Crop': crop,
        'Rainfall (mm)': rainfall,
        'Soil pH': x.iloc[i]['ph'],
        'Predicted Yield (tons/ha)': round(prediction, 1),
        'Yield Status': yield_status,
        'Rainfall Status': rainfall_status,
        'Planting Window': planting_window
    })

# Save to CSV
results_df = pd.DataFrame(results_data)
results_df.to_csv('results.csv', index=False)
print("Results saved to results.csv")

# Plot: Rainfall vs Predicted Yield
plt.figure(figsize=(10, 6))
plt.scatter(results_df['Rainfall (mm)'], results_df['Predicted Yield (tons/ha)'], 
            color='green', s=100, alpha=0.7, edgecolors='black')
plt.xlabel('Rainfall (mm)', fontsize=12)
plt.ylabel('Predicted Yield (tons/ha)', fontsize=12)
plt.title('FarmYield Predictor - Rainfall vs Yield Forecast', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('yield_forecast.png', dpi=300)
print("Forecast plot saved to yield_forecast.png")
plt.close()
