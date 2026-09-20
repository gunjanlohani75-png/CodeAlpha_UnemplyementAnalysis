# 📊 Unemployment Analysis with Python - CodeAlpha Internship

## 📌 Project Overview
This project is part of **CodeAlpha Data Science Internship - Task 2**.

The goal was to analyze unemployment in India from 2019 to 2020 and find the impact of COVID-19 lockdown on jobs.

**Live Repository:** https://github.com/gunjanlohani75-png/CodeAlpha_UnemplyementAnalysis

## 🎯 Objectives
- Analyze unemployment rate trend over time
- Study impact of COVID-19 lockdown (March - June 2020)
- Compare Rural vs Urban unemployment
- Find region-wise most affected states

## 📁 Dataset Used
- **File Name:** Unemployment_Rate_upto_11_2020.csv
- **Source:** Kaggle - Unemployment in India
- **Period:** May 2019 to Nov 2020
- **Columns:**
    - Region
    - Date
    - Frequency (Monthly)
    - Estimated Unemployment Rate (%)
    - Estimated Employed
    - Labour Participation Rate (%)
    - Area (Rural / Urban)

## 🛠️ Tech Stack & Libraries
- Python 3.10 / 3.14
- Pandas - Data Cleaning & Analysis
- Matplotlib - Visualization
- Seaborn - Statistical Graphs
- NumPy

## ⚙️ How to Run This Project

```bash
# 1. Install libraries
pip install pandas matplotlib seaborn numpy

# 2. Create dataset (if you don't have CSV)
python create_csv.py

# 3. Run main analysis
python unemployement_analysis.py
