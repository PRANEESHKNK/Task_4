# RTA_Accident_Analysis.py

import pandas as pd
import seaborn as sns
import folium
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('RTA Dataset.csv')

# Preview data
print(df.head())

# Remove duplicates
df.drop_duplicates(inplace=True)
print("Duplicated rows:", df.duplicated().sum())

# Day of week analysis
plt.figure(figsize=(6, 4))
sns.histplot(df['Day_of_week'], kde=True, bins=20)
plt.title('Days Of Week')
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.show()

# Hour of the day analysis
df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
plt.figure(figsize=(6, 4))
sns.countplot(x='Hour', data=df)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.show()

# Type of collision vs accident severity
plt.figure(figsize=(6, 4))
sns.countplot(x='Type_of_collision', data=df, hue='Accident_severity', palette='plasma',
              order=df['Type_of_collision'].value_counts().index)
plt.xlabel('Type of Collision')
plt.ylabel('Number of Accidents')
plt.title('Accidents by Type of Collision')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Road surface conditions vs causes
plt.figure(figsize=(6, 4))
sns.barplot(x='Road_surface_conditions', y='Cause_of_accident', data=df)
plt.xlabel('Road Surface Conditions')
plt.ylabel('Cause of Accident')
plt.title('Accidents by Road Surface Conditions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Accident severity histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['Accident_severity'], kde=True, bins=20)
plt.title('Accident Severity')
plt.xlabel('Severity')
plt.ylabel('Frequency')
plt.show()

# Numerical column check
numerical = [i for i in df.columns if df[i].dtype != 'O']
print('The numerical variables are:', numerical)

# Accident severity by weather conditions
plt.figure(figsize=(6, 4))
sns.countplot(x='Weather_conditions', data=df, hue='Accident_severity', palette='plasma',
              order=df['Weather_conditions'].value_counts().index)
plt.title('Accident Severity by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
