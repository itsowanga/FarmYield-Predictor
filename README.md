# FarmYield Predictor

> Smallholder farmers in rural South Africa face unpredictable crop yields due to variable rainfall, soil quality, and climate shifts, leading to food insecurity and lost income. Without affordable tools, they rely on guesswork, resulting in over/under-planting and wasted resources. Existing apps are urban/commercial-focused, data-heavy, and require constant internet  impractical for off-grid farms in areas like Sterkspruit.

> FarmYield Predictor is an offline-first C++/Python app that takes simple inputs (crop type, rainfall mm, soil pH, planting date), uses a lightweight ML model (linear regression on historical SA agri data) to predict yields (e.g., "Maize: 4.2 tons/ha"), and generates a printable planting calendar with risk alerts (e.g., "Low rain risk  plant drought-resistant variety"). Runs 100% offline after initial data load. Exports CSV for sharing via WhatsApp.

---

##  Dataset: South Africa Maize Yield Data

**File:** `data.csv`  
**Records:** 106 rows of maize crop data  
**Region:** South Africa (smallholder farms)

### Columns:
- **crop**  Crop type (Maize)
- **rainfall**  Annual rainfall in mm (280720 mm)
- **ph**  Soil pH (5.27.3)
- **yield_tons_per_ha**  Maize yield in tons per hectare (1.16.2 tons/ha)

### Key Statistics:
- **Average Yield:** 3.92 tons/ha
- **Rainfall Range:** 280720 mm (avg: 510 mm)
- **Soil pH Range:** 5.27.3 (avg: 6.37)
- **Rainfall-Yield Correlation:** 0.992 (very strong positive relationship)

---

##  Data Analysis Tool

**File:** `analyze_data.py`  
A Python utility to explore and visualize the maize yield dataset.

### Features:
1. **Load & Validate Data**  Reads `data.csv` using pandas
2. **Statistical Summary**  Displays avg yield, min/max rainfall, soil pH stats
3. **Filter by Crop**  Isolates maize records (extensible for other crops)
4. **Visualization**  Generates scatter plot: **Rainfall vs. Yield**
5. **Export Plot**  Saves visualization as `test.png` (300 DPI)

### Usage:
```bash
python analyze_data.py
```

### Requirements:
- Python 3.8+
- pandas
- matplotlib

### Output:
- Console: Formatted statistics table
- Image: `test.png`  Scatter plot with correlation coefficient

---

##  Getting Started

1. Clone the repository
2. Install Python dependencies: `pip install pandas matplotlib`
3. Run the analysis: `python analyze_data.py`
4. View the generated plot: `test.png`

---

##  Model Training

**File:** `train.py`  
Trains a linear regression model on the maize yield dataset.

### Process:
1. **Load Data**  Reads `data.csv`
2. **Feature Selection**  Uses rainfall and soil pH as predictors
3. **Target Variable**  Maize yield (tons/ha)
4. **Train-Test Split**  80/20 split for validation
5. **Model**  Linear regression (scikit-learn)
6. **Save Model**  Exports trained model to `model.joblib`

### Usage:
```bash
python train.py
```

### Output:
- **model.joblib**  Trained ML model (used by predictor)
- Console: Model performance metrics (R², MSE)

---

##  Prediction & Actionable Insights

**File:** `predict.py`  
Generates yield predictions, risk alerts, and farmer-friendly outputs.

### Input:
- **File:** `input.txt` (CSV format: crop, rainfall, pH)
- **Example:**
  ```
  Maize,450,6.5
  Maize,380,5.8
  Maize,520,6.2
  ```

### Process:
1. **Load Predictions**  Reads farmer inputs from `input.txt`
2. **Run ML Model**  Predicts yield using trained `model.joblib`
3. **Risk Assessment**  
   - If predicted yield < 3.0 tons/ha → "LOW YIELD RISK"
   - If rainfall < 400 mm → "Consider drought-resistant seed"
4. **Generate Outputs:**
   - **results.csv**  All inputs + predictions + risk status + planting calendar
   - **yield_forecast.png**  Scatter plot visualization (Rainfall vs. Predicted Yield)

### Usage:
```bash
python predict.py
```

### Output Files:
- **results.csv**  Farmer-ready data (importable in LibreOffice, shareable via email/WhatsApp)
- **yield_forecast.png**  Visual forecast (300 DPI, offline-friendly)

### CSV Columns:
| Crop | Rainfall (mm) | Soil pH | Predicted Yield (tons/ha) | Yield Status | Rainfall Status | Planting Window |
|------|---------------|---------|---------------------------|--------------|-----------------|-----------------|
| Maize | 450 | 6.5 | 3.6 | Good yield expected | Rainfall is adequate | October - November |
| Maize | 380 | 5.8 | 2.4 | LOW YIELD RISK | Low rainfall - Consider drought-resistant seed | October - November |

---

##  Data Input Tool

**File:** `fdata.cpp`  
C++ command-line interface for farmers to input crop data.

### Features:
1. **Interactive Input**  Prompts for crop type, rainfall (mm), and soil pH
2. **Validation**  Ensures soil pH is within 4.0–8.0 range
3. **Batch Processing**  Collect multiple farm records in one session
4. **CSV Export**  Saves inputs to `input.txt` for Python processing

### Usage:
```bash
g++ -o fdata fdata.cpp
./fdata.exe
```

### Input Flow:
```
Enter data (space separated) or 'exit' to quit:
Maize 450 6.5
```

### Output:
- **input.txt**  CSV file ready for `predict.py`

---

##  Complete Workflow

### Step 1: Collect Data
```bash
./fdata.exe
# Enter: Maize 450 6.5
# Saves to input.txt
```

### Step 2: Generate Predictions & Insights
```bash
python predict.py
# Outputs: results.csv, yield_forecast.png
```

### Step 3: Share Results
- Open `results.csv` in **LibreOffice Calc** (offline)
- View forecast graph `yield_forecast.png`
- Share CSV via **WhatsApp, email, or print**

---

##  Model Performance

The strong rainfall-yield correlation (r = 0.992) indicates that rainfall is an excellent predictor of maize yield in South African smallholder farming contexts. This validates the use of linear regression for the FarmYield Predictor's yield forecasting engine.

### Key Insights:
- **Rainfall is Critical**  400 mm threshold separates adequate vs. drought-risk scenarios
- **Soil pH Matters**  Optimal pH range is 6.0–7.0 for maize
- **Linear Model Sufficient**  No need for complex algorithms in offline environment

---

##  Technology Stack

- **Backend**  Python 3.8+ (scikit-learn, pandas, matplotlib)
- **Data Input**  C++ (lightweight, portable)
- **ML Model**  Linear Regression (scikit-learn)
- **Data Format**  CSV (universal, offline-friendly)
- **Visualization**  Matplotlib (PNG export)
- **Requirements**  No internet, works offline after initial setup

---

##  Files Overview

| File | Purpose |
|------|---------|
| `data.csv` | Historical SA maize yield dataset (106 records) |
| `analyze_data.py` | Explore & visualize dataset |
| `train.py` | Train ML model → `model.joblib` |
| `predict.py` | Predict yields & generate outputs |
| `fdata.cpp` | Data input tool for farmers |
| `input.txt` | Farmer inputs (CSV format) |
| `results.csv` | Predictions + risk alerts (shareable) |
| `yield_forecast.png` | Visualization of yield forecast |
| `model.joblib` | Trained ML model (binary) |

---

##  Future Enhancements

- [ ] Support multiple crops (Beans, Sorghum, Wheat)
- [ ] Add temperature & humidity inputs
- [ ] Mobile app wrapper (offline-first)
- [ ] Audio input for low-literacy farmers
- [ ] SMS delivery of results
- [ ] Multi-language support (Sotho, Xhosa, Zulu)

---

##  License

MIT License - Open source for agricultural development

---

## Contact & Support

For issues or suggestions, contact: sowanga.mbane@gmail.com/@itsowanga at github.com

**Mission:** Empower smallholder farmers in rural South Africa with affordable, offline-first yield prediction technology.
