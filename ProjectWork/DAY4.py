import csv

# Farmer Guardian Project - Part 4 (CSV Storage)

# Taking input
name = input("Enter your name: ")
location = input("Enter your location: ")
crop = input("Enter the crop you are growing: ")

temperature = float(input("Enter current temperature (°C): "))
rainfall = float(input("Enter current rainfall (mm): "))

# Farming advice system
advice = []
if temperature > 35:
    advice.append("High temperature: Consider irrigation.")
elif temperature < 15:
    advice.append("Low temperature: Protect crops from cold stress.")
else:
    advice.append("Temperature is within healthy range.")

if rainfall < 50:
    advice.append("Low rainfall: Use drip irrigation.")
elif rainfall > 200:
    advice.append("Heavy rainfall: Ensure proper drainage.")
else:
    advice.append("Rainfall is adequate.")

if temperature > 35 and rainfall < 50:
    advice.append("🚨 ALERT: Drought risk (Hot + Low Rainfall)!")

crop_advice = {
    "wheat": "Wheat grows best in cool climate with moderate rainfall.",
    "rice": "Rice needs standing water. Ensure sufficient irrigation.",
    "sugarcane": "Sugarcane requires plenty of sunlight and water.",
    "cotton": "Cotton needs warm climate and less waterlogging."
}

if crop.lower() in crop_advice:
    advice.append(crop_advice[crop.lower()])
else:
    advice.append("General advice: Follow local farming guidelines.")

# Prepare row for CSV
row = [name, location, crop, temperature, rainfall, " | ".join(advice)]

# Write to CSV file
with open("farmer_data.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Write header only if file is empty
    if f.tell() == 0:
        writer.writerow(["Name", "Location", "Crop", "Temperature (°C)", "Rainfall (mm)", "Advice"])

    # Write farmer data
    writer.writerow(row)

print("\n✅ Farmer details and advice saved in 'farmer_data.csv'")
