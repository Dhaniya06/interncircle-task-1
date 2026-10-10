import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            print(f"\nWeather in {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Feels like: {data['main']['feels_like']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Conditions: {data['weather'][0]['description'].title()}")
            print(f"Wind speed: {data['wind']['speed']} m/s")
        else:
            print("Error:", data.get("message", "Unable to fetch weather."))

    except requests.RequestException as error:
        print("Network error:", error)


if __name__ == "__main__":
    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")
