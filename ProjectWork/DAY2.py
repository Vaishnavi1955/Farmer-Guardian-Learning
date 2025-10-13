# Farmer Guardian Project - Part 2 & Bonus

# Taking input from farmer
name = input("Enter your name: ")
location = input("Enter your location: ")
crop = input("Enter the crop you are growing: ")

# Weather details
temperature = float(input("Enter current temperature (°C): "))
rainfall = float(input("Enter current rainfall (mm): "))

# Display summary
print("\n--- Farmer Information Summary ---")
print(f"Name: {name}")
print(f"Location: {location}")
print(f"Crop: {crop}")
print(f"Temperature: {temperature}°C")
print(f"Rainfall: {rainfall} mm")

# Farming advice system
print("\n--- Farming Advice ---")

# Temperature advice
if temperature > 35:
    print("⚠️ High temperature detected! Consider irrigation.")
elif temperature < 15:
    print("❄️ Low temperature detected! Protect crops from cold stress.")
else:
    print("✅ Temperature is within a healthy range.")

# Rainfall advice
if rainfall < 50:
    print("💧 Low rainfall: Use water-saving techniques like drip irrigation.")
elif rainfall > 200:
    print("🌊 Heavy rainfall: Ensure proper drainage to avoid waterlogging.")
else:
    print("☔ Rainfall is adequate for crop growth.")

# Combined condition example
if temperature > 35 and rainfall < 50:
    print("🚨 ALERT: Hot weather + low rainfall → High drought risk!")

# Crop-specific advice (dictionary-based)
crop_advice = {
    "wheat": "🌾 Wheat grows best in cool climate with moderate rainfall.",
    "rice": "🍚 Rice needs standing water. Ensure sufficient irrigation.",
    "sugarcane": "🪵 Sugarcane requires plenty of sunlight and water.",
    "cotton": "👕 Cotton needs warm climate and less waterlogging."
}

if crop.lower() in crop_advice:
    print(crop_advice[crop.lower()])
else:
    print("📌 General advice: Ensure proper care based on local guidelines.")
