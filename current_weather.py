#!/usr/bin/env python3
from datetime import datetime
import requests
import math

# ---------------- CONFIGURATION ----------------

# API_KEY = "YOUR_API_KEY_HERE"  # <-- put your OpenWeatherMap API key here
API_KEY = "f6f1f7f9005c0f83b9a37b6b42a92ab7"  
CITIES = [
    "Victoria, CA",
    "Vancouver, CA",
    "Kelowna, CA",
    "Calgary, CA",
    "Edmonton, CA",
    "Regina, CA",
    "Saskatoon, CA",
    "Winnipeg, CA",
    "Brandon, CA",
    "Huntsville, CA",
    "Sauble Beach, CA",
    "Guelph, CA",
    "Hamilton, CA",
    "Caledon, CA",
    "Toronto, CA",
    "Mississauga, CA",
    "St. Catharines, CA",
    "Ottawa, CA",
    "Montreal, CA",
    "Quebec City, CA",
    "Charlottetown, CA",
    "Halifax, CA",
    "St. John's, CA",
]

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ---------------- HELPERS ----------------

def round_temp(x):
    """Canadian-style rounding: .5 always away from zero"""
    return int(x + 0.5) if x >= 0 else int(x - 0.5)

def wind_chill(temp_c, wind_kmh):
    """Canadian wind chill formula"""
    return (
        13.12
        + 0.6215 * temp_c
        - 11.37 * (wind_kmh ** 0.16)
        + 0.3965 * temp_c * (wind_kmh ** 0.16)
    )

def humidex(temp_c, humidity):
    """Canadian humidex formula"""
    e = 6.112 * math.exp((17.67 * temp_c) / (temp_c + 243.5)) * (humidity / 100)
    return temp_c + (5 / 9) * (e - 10)

# ---------------- WEATHER FETCH ----------------

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        r = requests.get(BASE_URL, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_ms = data["wind"]["speed"]
        wind_kmh = wind_ms * 3.6

        feels_like = None
        feels_label = ""

        if temp <= 10 and wind_kmh >= 4.8:
            feels_like = wind_chill(temp, wind_kmh)
            feels_label = "Wind Chill"
        elif temp >= 20:
            feels_like = humidex(temp, humidity)
            feels_label = "Humidex"

        return {
            "temp": temp,
            "condition": data["weather"][0]["description"].title(),
            "humidity": humidity,
            "wind_kmh": wind_kmh,
            "feels_like": feels_like,
            "feels_label": feels_label
        }

    except Exception as e:
        return {"error": str(e)}

# ---------------- MAIN ----------------

def main():
# Print current date and time with a blank line
    now = datetime.now()
    print(f"\nWeather Across Canada")
    print(f"Observation Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
    header = (
        f"{'City':18} | "
        f"{'Temp':>4}  | "
        f"{'Conditions':20} | "
        f"{'RH':>3}  | "
        f"{'Wind (km/h)':>10}| "
        f"{'Feels Like':>11}"
    )

    separator = "-" * len(header)+"-----"

    print(header)
    print(separator)

    for city in CITIES:
        weather = get_weather(city)

        if "error" in weather:
            print(f"{city:18} | Error: {weather['error']}")
            continue

        temp_str = f"{round_temp(weather['temp']):>3}°C"

        feels_str = ""
        if weather["feels_like"] is not None:
            feels_str = (
                f"{weather['feels_label']} "
                f"{round_temp(weather['feels_like']):>3}°C"
            )

        print(
            f"{city:18} | "
            f"{temp_str:>4} | "
            f"{weather['condition']:<20} | "
            f"{weather['humidity']:>3}% | "
            f"{weather['wind_kmh']:>6.1f}     | "
            f"{feels_str:>11}"
        )
    print (f" ")

# ---------------- ENTRY POINT ----------------

if __name__ == "__main__":
    main()

