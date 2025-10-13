# Farmer Guardian Project - Part 3 (File Storage)

# Taking input
name = input("Enter your name: ")
location = input("Enter your location: ")
crop = input("Enter the crop you are growing: ")

temperature = float(input("Enter current temperature (°C): "))
rainfall = float(input("Enter current rainfall (mm): "))

# Farming advice system
advice = []
if temperature > 35:
    advice.append("⚠️ High temperature: Consider irrigation.")
elif temperature < 15:
    advice.append("❄️ Low temperature: Protect crops from cold stress.")
else:
    advice.append("✅ Temperature is within healthy range.")

if rainfall < 50:
    advice.append("💧 Low rainfall: Use drip irrigation.")
elif rainfall > 200:
    advice.append("🌊 Heavy rainfall: Ensure proper drainage.")
else:
    advice.append("☔ Rainfall is adequate.")

if temperature > 35 and rainfall < 50:
    advice.append("🚨 ALERT: Drought risk (Hot + Low Rainfall)!")

crop_advice = {
    "wheat": "🌾 Wheat grows best in cool climate with moderate rainfall.",
    "rice": "🍚 Rice needs standing water. Ensure sufficient irrigation.",
    "sugarcane": "🪵 Sugarcane requires plenty of sunlight and water.",
    "cotton": "👕 Cotton needs warm climate and less waterlogging."
}

if crop.lower() in crop_advice:
    advice.append(crop_advice[crop.lower()])
else:
    advice.append("📌 General advice: Follow local farming guidelines.")

# Save to file
with open("farmer_data.txt", "a", encoding="utf-8") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Location: {location}\n")
    f.write(f"Crop: {crop}\n")
    f.write(f"Temperature: {temperature}°C\n")
    f.write(f"Rainfall: {rainfall} mm\n")
    f.write("Advice:\n")
    for a in advice:
        f.write(f" - {a}\n")
    f.write("-" * 40 + "\n")

print("\n✅ Farmer details and advice saved in 'farmer_data.txt'")
