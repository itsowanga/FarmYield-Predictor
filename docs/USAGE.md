# FarmYield Predictor - Usage Guide

## Quick Start (3 Steps)

### 1️⃣ Input Farm Data
Run the data input tool:
```bash
./src/fdata.exe
```
Or create `data/input.txt` manually:
```
Maize,450,6.5
Beans,380,6.2
```

### 2️⃣ Generate Predictions
```bash
python src/predict.py
```

### 3️⃣ View Results
- Open `output/results.csv` in LibreOffice Calc
- View `output/yield_forecast.png` for visualization

---

## Understanding the Output

### results.csv Columns

| Column | Meaning | Example |
|--------|---------|---------|
| Crop | Crop type | Maize |
| Rainfall (mm) | Annual rainfall | 450 |
| Soil pH | Soil acidity | 6.5 |
| Predicted Yield (tons/ha) | Expected harvest | 3.6 |
| Yield Status | Risk level | Good yield expected |
| Rainfall Status | Water availability | Rainfall is adequate |
| Planting Window | Best planting dates | October - November |

### Risk Alerts

**LOW YIELD RISK** (Yield < 3.0 tons/ha)
- Indicates below-average expected harvest
- Action: Consider supplementary irrigation or high-yield varieties

**Low Rainfall Alert** (Rainfall < 400 mm)
- Indicates drought risk
- Action: Plant drought-resistant seed varieties

---

## Data Input Format

### Via C++ Tool (`fdata.exe`)
```
Enter data (space separated) or 'exit' to quit:
Maize 450 6.5
```

### Direct CSV Format (`data/input.txt`)
```
Crop,Rainfall,pH
Maize,450,6.5
Beans,380,6.2
Sorghum,320,5.9
```

**Validation Rules:**
- Rainfall: 280–720 mm (optional, adjust as needed)
- Soil pH: 4.0–8.0 (enforced in C++ tool)

---

## Sharing Results

### 1. Via WhatsApp
- Attach `output/results.csv` to message
- Screenshot `output/yield_forecast.png`

### 2. Via Email
- Send `output/results.csv` as attachment
- Include chart image

### 3. Print for Offline Distribution
- Print `output/results.csv` (CSV-friendly)
- Print `output/yield_forecast.png` for visual reference

---

## Customizing Thresholds

Edit `src/predict.py` to change risk levels:

```python
# Line 45-48: Yield risk threshold
if prediction < 3.0:  # Change 3.0 to desired threshold
    yield_status = "LOW YIELD RISK"

# Line 51-54: Rainfall risk threshold
if rainfall < 400:  # Change 400 to desired threshold
    rainfall_status = "Low rainfall - Consider drought-resistant seed"
```

---

## Troubleshooting

### Problem: "File not found" error
**Solution:** Ensure `data/input.txt` exists and has correct format

### Problem: Model predictions are way off
**Solution:** Retrain model with `python src/train.py`

### Problem: CSV won't open in LibreOffice
**Solution:** Use "Text to Columns" feature, select comma delimiter

---

## Example Workflow

```bash
# 1. Prepare environment
pip install -r requirements.txt

# 2. Train model (one-time)
python src/train.py

# 3. Input farm data
./src/fdata.exe
# Enter: Maize 450 6.5
# Enter: Beans 380 6.2
# Enter: exit

# 4. Generate predictions
python src/predict.py

# 5. View results
# Open output/results.csv in LibreOffice Calc
# View output/yield_forecast.png
```

---

## Advanced Usage

### Batch Processing Multiple Farms
1. Create `data/input.txt` with all farm records
2. Run `python src/predict.py`
3. All predictions in one CSV file

### Analyzing Historical Performance
```bash
python src/analyze_data.py
```
Generates statistical summary and visualization

---

## Contact & Support

For issues or feature requests:
- GitHub: https://github.com/itsowanga/FarmYield-Predictor
- Email: [Your Email]

---

**Happy farming! 🌾**
