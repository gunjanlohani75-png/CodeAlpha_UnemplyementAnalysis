import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Check file exists
files = os.listdir('.')
print("Files in folder:", files)

# Try both possible names
filename = None
for name in ['Unemployment_Rate_upto_11_2020.csv', 'Unemployment in India.csv', 'unemployment.csv']:
    if name in files:
        filename = name
        break

if filename is None:
    print("ERROR: CSV file not found! Please download the dataset and put in this folder.")
    exit()

print(f"Loading file: {filename}")
df = pd.read_csv(filename)

# Clean columns
df.columns = df.columns.str.strip()
print("Columns:", df.columns.tolist())
print(df.head())

# Clean column names with space issue
rate_col = [c for c in df.columns if 'Unemployment Rate' in c][0]
date_col = [c for c in df.columns if 'Date' in c][0]

print(f"\nAverage Unemployment Rate: {df[rate_col].mean():.2f}%")

# Plot 1: Trend
plt.figure(figsize=(12,5))
# Use only last 100 rows for better view if data too big
sns.lineplot(data=df, x=date_col, y=rate_col)
plt.title('Unemployment Rate Over Time in India')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('trend.png')
print("Saved trend.png")
plt.show()

# Plot 2: Region wise
if 'Region' in df.columns:
    plt.figure(figsize=(10,5))
    sns.barplot(data=df, x='Region', y=rate_col, estimator='mean')
    plt.title('Region wise Unemployment')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('region.png')
    print("Saved region.png")
    plt.show()

# Plot 3: Rural vs Urban
if 'Area' in df.columns:
    plt.figure()
    sns.boxplot(data=df, x='Area', y=rate_col)
    plt.title('Rural vs Urban Unemployment')
    plt.tight_layout()
    plt.savefig('rural_urban.png')
    print("Saved rural_urban.png")
    plt.show()

print("Task 2 Completed Successfully!")