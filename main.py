
import requests

API_KEY = "32807dad06451c9ad08f2be89899cccd"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 404:
            print("City not found. Check the city name.")
            return

        response.raise_for_status()
        data = response.json()

        print("\n--- Current Weather ---")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"].title())

    except requests.exceptions.HTTPError as error:
        print("Weather API error:", error)
        print("Check that your API key is active.")

    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection.")

    except (KeyError, ValueError):
        print("Could not process the weather data.")


def main():
    print("=== InternCircle Weather App ===")

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Goodbye!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
