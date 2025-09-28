#farmers info collector
#taking input from farmer
name=input("Enter your name")
location=input("Enter your location: ")
crop=input("Enter the crop you are growing: ")

#for now,ask waether details manuaaly
temperature=float(input("Enter current temperature(°C): "))
rainfall=float(input("Enter current rainfall(mm): "))

# Display summary
print("\n--- Farmer Information Summary ---")
print(f"Name: {name}")
print(f"Location: {location}")
print(f"Crop: {crop}")
print(f"Temperature: {temperature}°C")
print(f"Rainfall: {rainfall} mm")

#Farming advice system
print("\n--- Farming Advice ---")

#Tempreature based advice
if temperature>35:
    print("⚠️ High temperature detected! Consider irrigation.")
elif temperature<15:
    print("❄️ Low temperature detected! Protect crops from frost.")
else:
    print("🌤️ Temperature is optimal for crop growth.")


#Rainfall based advice
if rainfall<50:
    print("💧 Low rainfall detected! Consider irrigation:Use water saving techniques like drip irrigations")
elif rainfall>200:
    print("🌧️ High rainfall detected! Ensure proper drainage to prevent waterlogging.")    
else:
    print("🌦️ Rainfall is adequate for crop growth.")

#combined advice
if temperature>30 and rainfall<50:
    print("🔥💧 Hot and dry conditions! Prioritize irrigation and mulching to retain soil moisture.")

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
    print("🌱 General crop advice: Regularly monitor soil moisture and weather conditions.")
print("\nThank you for using the Farming Advice System! Happy Farming! 🌾🚜")