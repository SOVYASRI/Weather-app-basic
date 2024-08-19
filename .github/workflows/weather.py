import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']

        print(f"Weather in {city_name}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found or there was an error in retrieving the data.")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    api_key = "f75e903c153667c7f395a386adf68601"
    get_weather(city_name, api_key)
