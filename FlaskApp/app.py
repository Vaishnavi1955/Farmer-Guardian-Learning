from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

CSV_FILE = "farmer_data.csv"

# Ensure CSV exists
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Name", "Location", "Crop", "Temperature", "Rainfall", "Advice"])
    df.to_csv(CSV_FILE, index=False)

# Ensure 'static' folder exists (needed later for charts)
if not os.path.exists("static"):
    os.makedirs("static")

# -----------------------------
# Home Page / Farmer Input
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        location = request.form.get("location", "").strip()
        crop = request.form.get("crop", "").strip()

        # Validate numeric input
        try:
            temperature = float(request.form.get("temperature", 0))
            rainfall = float(request.form.get("rainfall", 0))
        except ValueError:
            return render_template("index.html", success=False, error="Please enter valid numbers for temperature and rainfall.")

        # Generate advice
        advice = []

        if temperature > 35 and rainfall < 50:
            advice.append("🚨 ALERT: Drought risk! Consider irrigation and drip system.")
        elif temperature > 35:
            advice.append("High temperature: Consider irrigation.")
        elif rainfall < 50:
            advice.append("Low rainfall: Use drip irrigation.")

        crop_advice = {
            "Wheat": "Wheat grows best in cool climate.",
            "Rice": "Rice needs standing water.",
            "Cotton": "Cotton needs warm climate.",
            "Sugarcane": "Sugarcane requires sunlight and water."
        }
        if crop in crop_advice:
            advice.append(crop_advice[crop])

        # Save to CSV
        df = pd.read_csv(CSV_FILE)
        df.loc[len(df)] = [name, location, crop, temperature, rainfall, " | ".join(advice)]
        df.to_csv(CSV_FILE, index=False)

        return render_template("index.html", success=True, advice=advice)

    return render_template("index.html", success=False)

# -----------------------------
# Charts Page (disabled for now)
# -----------------------------
# @app.route("/charts")
# def charts():
#     df = pd.read_csv(CSV_FILE)
#     # Chart generation code goes here later
#     return render_template("charts.html")

# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
