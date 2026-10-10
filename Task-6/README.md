Weather App with Live OpenWeather API

Description

A Python application that fetches real-time weather information for a city using the OpenWeather API.

Features

- Fetches live weather data for a given city.
- Displays temperature in Celsius.
- Shows feels-like temperature and humidity.
- Displays weather conditions and wind speed.
- Handles invalid city names and network errors.

Technologies Used

- Python
- Requests library
- OpenWeather API
- JSON response parsing

Installation

Install the required library:

pip install -r requirements.txt

API Key Setup

1. Create an account at https://openweathermap.org/
2. Generate an API key.
3. Replace "YOUR_OPENWEATHER_API_KEY" in "weather_app.py" with your API key.
4. Keep your API key private. Do not upload your real key to GitHub.

Run the Application

python weather_app.py

Enter a city name when prompted to view its current weather.

Note

An active OpenWeather API key and an internet connection are required.
