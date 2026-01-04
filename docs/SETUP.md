# FarmYield Predictor - Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- G++ compiler (for C++ data input tool)
- LibreOffice Calc (optional, for viewing results)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/itsowanga/FarmYield-Predictor.git
cd FarmYield-Predictor
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Compile C++ Data Input Tool (Optional)
```bash
cd src
g++ -o fdata fdata.cpp
cd ..
```

## Running the Application

### Step 1: Prepare Training Data
Ensure `data/data.csv` exists with columns: `crop`, `rainfall`, `ph`, `yield_tons_per_ha`

### Step 2: Train the Model
```bash
python src/train.py
```
This creates `models/model.joblib`

### Step 3: Input Farm Data
Option A - Interactive input (C++):
```bash
./src/fdata.exe
# Follow prompts to enter crop, rainfall, soil pH
```

Option B - Direct CSV:
Create `data/input.txt` with format:
```
Maize,450,6.5
Maize,380,5.8
```

### Step 4: Generate Predictions & Calendar
```bash
python src/predict.py
```

### Step 5: View Results
- **Predictions**: Open `output/results.csv` in LibreOffice Calc
- **Visualization**: View `output/yield_forecast.png`

## File Structure

```
FarmYield-Predictor/
├── src/                  # Source code
│   ├── train.py         # Model training
│   ├── predict.py       # Predictions & insights
│   ├── analyze_data.py  # Data analysis
│   └── fdata.cpp        # Data input tool
├── data/                # Data files
│   ├── data.csv         # Historical dataset
│   └── input.txt        # User inputs
├── models/              # Trained ML models
│   └── model.joblib     # Trained model
├── output/              # Generated outputs
│   ├── results.csv      # Predictions (shareable)
│   └── yield_forecast.png  # Visualization
├── docs/                # Documentation
├── requirements.txt     # Python dependencies
├── README.md           # Project overview
├── LICENSE             # MIT License
└── .gitignore          # Git ignore rules
```

## Troubleshooting

### Python module not found
```bash
pip install --upgrade -r requirements.txt
```

### Model file not found
Ensure you've run `python src/train.py` first

### C++ compilation fails
Install MinGW or use Windows Visual C++ compiler

## Next Steps

- Read `README.md` for project overview
- Check `docs/USAGE.md` for detailed workflow
- Modify thresholds in `src/predict.py` if needed

---

**Need help?** Open an issue on [GitHub](https://github.com/itsowanga/FarmYield-Predictor/issues)
