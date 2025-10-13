import pandas as pd

# Farmer Guardian Project - Part 5 (Data Analysis)

# Load farmer data
df = pd.read_csv("D:/aiml/PythonCourse/ProjectWork/farmer_data.csv")


print("✅ Farmer data loaded successfully!\n")

# Show first few records
print("📋 Farmer Records:")
print(df.head(), "\n")

# Basic info
print("🔎 Dataset Info:")
print(df.info(), "\n")

# Total farmers recorded
print(f"👨‍🌾 Total Farmers: {len(df)}")

# Crops distribution
print("\n🌾 Crop Distribution:")
print(df['Crop'].value_counts())

# Average temperature & rainfall
print("\n🌡️ Average Temperature:", df['Temperature (°C)'].mean())
print("☔ Average Rainfall:", df['Rainfall (mm)'].mean())

# Which locations reported drought alerts
print("\n🚨 Drought Risk Cases:")
drought_cases = df[df['Advice'].str.contains("Drought risk", na=False)]
print(drought_cases[['Name', 'Location', 'Crop']])
