import requests
import pandas as pd
import matplotlib.pyplot as plt

#API key and city name
API_KEY = "d780eb773b1c633ec5c20038e579803a"
CITY = "Kolkata"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetching the weather data
response = requests.get(URL)
data = response.json()
timestamps = []
temperatures = []

# Processing the data
for entry in data["list"]:
    timestamps.append(entry["dt_txt"])
    temperatures.append(entry["main"]["temp"])
df = pd.DataFrame({"Time": timestamps, "Temperature": temperatures})

# Plotting the data
plt.figure(figsize=(12,5))
plt.plot(df["Time"], df["Temperature"])
plt.xticks(rotation=45)
plt.title("Temperature Forecast")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()