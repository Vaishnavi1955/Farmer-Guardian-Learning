import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("farmer_data.csv")

# -----------------------------
# 1️⃣ Crop Distribution (Bar Chart)
# -----------------------------
crop_counts = df['Crop'].value_counts()
plt.figure(figsize=(6,4))
crop_counts.plot(kind='bar', color='skyblue')
plt.title("Crop Distribution Among Farmers")
plt.xlabel("Crop")
plt.ylabel("Number of Farmers")
plt.xticks(rotation=0)
plt.show()

# -----------------------------
# 2️⃣ Farmers per Location (Pie Chart)
# -----------------------------
location_counts = df['Location'].value_counts()
plt.figure(figsize=(6,6))
location_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Farmers by Location")
plt.ylabel("")
plt.show()

# -----------------------------
# 3️⃣ Temperature vs Rainfall (Scatter Plot)
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(df['Temperature (°C)'], df['Rainfall (mm)'], color='green')
plt.title("Temperature vs Rainfall")
plt.xlabel("Temperature (°C)")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()
