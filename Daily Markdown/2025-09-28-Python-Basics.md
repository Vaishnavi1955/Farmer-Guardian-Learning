# 2025-09-28
## Topic: Farmer Guardian Project – Part 1 (Farmer Info Collector)

### What I Learned Today
- How to take input from users using `input()`
- Using variables to store information
- Data types: `str`, `float`, `int`
- Converting user input into correct data type (e.g., `float()` for numbers)
- Printing formatted output using **f-strings**
- Structured coding for a simple project
- **If-else statements:** Making decisions based on conditions
- **Comparison operators:** `>`, `<`, `==`, `!=`
- **Logical operators:** `and`, `or`
- **Dictionaries:** Used for storing crop-specific advice
- **String methods:** `.lower()` for case-insensitive checks
- **Combined conditions:** Handling multiple weather risks together
---

### Project Code: Farmer Info Collector

```python
# Farmer Info Collector (Part 1)

# Taking input from farmer
name = input("Enter your name: ")
location = input("Enter your location: ")
crop = input("Enter the crop you are growing: ")

# For now, ask weather details manually
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
