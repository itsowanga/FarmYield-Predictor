import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Read data.csv with pandas
print("Loading data.csv...")
df = pd.read_csv('data.csv')
print(f"Data loaded successfully. Shape: {df.shape}\n")

# Task 2: Print statistics - avg yield, min/max rain
print("=" * 60)
print("DATA STATISTICS")
print("=" * 60)
avg_yield = df['yield_tons_per_ha'].mean()
min_rainfall = df['rainfall'].min()
max_rainfall = df['rainfall'].max()
avg_rainfall = df['rainfall'].mean()
min_yield = df['yield_tons_per_ha'].min()
max_yield = df['yield_tons_per_ha'].max()
avg_ph = df['ph'].mean()

print(f"Average Yield: {avg_yield:.2f} tons/ha")
print(f"Min Yield: {min_yield:.2f} tons/ha")
print(f"Max Yield: {max_yield:.2f} tons/ha")
print()
print(f"Minimum Rainfall: {min_rainfall:.0f} mm")
print(f"Maximum Rainfall: {max_rainfall:.0f} mm")
print(f"Average Rainfall: {avg_rainfall:.2f} mm")
print()
print(f"Average Soil pH: {avg_ph:.2f}")
print(f"Total Records: {len(df)}")
print()

# Task 3: Filter only maize rows
print("=" * 60)
print("FILTERING MAIZE ROWS")
print("=" * 60)
maize_df = df[df['crop'] == 'Maize']
print(f"Maize rows: {len(maize_df)} out of {len(df)} total rows")
print(f"Crops in dataset: {df['crop'].unique()}\n")

# Task 4: Plot rainfall vs yield and save as test.png
print("=" * 60)
print("GENERATING PLOT")
print("=" * 60)
plt.figure(figsize=(10, 6))
plt.scatter(maize_df['rainfall'], maize_df['yield_tons_per_ha'], 
            alpha=0.6, s=50, color='darkgreen', edgecolors='black', linewidth=0.5)
plt.xlabel('Rainfall (mm)', fontsize=12, fontweight='bold')
plt.ylabel('Yield (tons/ha)', fontsize=12, fontweight='bold')
plt.title('South Africa Maize: Rainfall vs Yield', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')

# Add correlation coefficient to the plot
correlation = maize_df['rainfall'].corr(maize_df['yield_tons_per_ha'])
plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
         transform=plt.gca().transAxes, fontsize=11, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('test.png', dpi=300, bbox_inches='tight')
print("Plot saved as 'test.png'")
print(f"Rainfall-Yield Correlation: {correlation:.3f}\n")

print("=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)
