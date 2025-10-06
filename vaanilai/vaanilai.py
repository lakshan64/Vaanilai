import requests
import pandas as pd

def get_weather(lat, lon):
    # Open-Meteo API endpoint
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Parameters: choose what data you want
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "current_weather": True
    }
    
    # Make the request
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Current weather
        current = data.get("current_weather", {})
        print("\n🌍 Current Weather")
        print(f"Temperature: {current.get('temperature')}°C")
        print(f"Windspeed: {current.get('windspeed')} km/h")
        print(f"Time: {current.get('time')}")
        
        # Hourly forecast into DataFrame
        hourly = data.get("hourly", {})
        df = pd.DataFrame({
            "time": hourly.get("time", []),
            "temperature": hourly.get("temperature_2m", []),
            "humidity": hourly.get("relative_humidity_2m", []),
            "wind_speed": hourly.get("wind_speed_10m", [])
        })
        
        print("\n📊 First 5 rows of forecast:")
        print(df.head())
    else:
        print("❌ Error:", response.status_code)

if __name__ == "__main__":
    # Example: Chennai coordinates
    get_weather(13.0827, 80.2707)
