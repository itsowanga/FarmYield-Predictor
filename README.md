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

##  Model Performance

The strong rainfall-yield correlation (r = 0.992) indicates that rainfall is an excellent predictor of maize yield in South African smallholder farming contexts. This validates the use of linear regression for the FarmYield Predictor's yield forecasting engine.
