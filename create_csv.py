import pandas as pd
import numpy as np

regions = ['Andhra Pradesh','Bihar','Delhi','Gujarat','Haryana','Karnataka','Maharashtra','Punjab','Rajasthan','Tamil Nadu','Uttar Pradesh','West Bengal']
areas = ['Rural','Urban']
data = []
start_date = pd.date_range(start='2019-05-31', end='2020-11-30', freq='ME')
np.random.seed(42)
for date in start_date:
    for region in regions:
        for area in areas:
            base = 7.5
            if date >= pd.Timestamp('2020-03-01') and date <= pd.Timestamp('2020-06-30'):
                base = np.random.uniform(15, 25) if area == 'Urban' else np.random.uniform(12, 20)
            elif date >= pd.Timestamp('2020-07-01'):
                base = np.random.uniform(8, 12)
            else:
                base = np.random.uniform(5, 10)
            data.append({
                'Region': region,
                ' Date': date.strftime('%d-%m-%Y'),
                ' Frequency': ' Monthly',
                ' Estimated Unemployment Rate (%)': round(base + np.random.uniform(-1,1), 2),
                ' Estimated Employed': int(np.random.randint(1000000, 5000000)),
                ' Estimated Labour Participation Rate (%)': round(float(np.random.uniform(40, 50)), 2),
                'Area': area
            })
df = pd.DataFrame(data)
df.to_csv('Unemployment_Rate_upto_11_2020.csv', index=False)
print("CSV Created Successfully!")