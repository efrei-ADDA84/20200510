import os
import requests

class WeatherWrapper:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self, lat, lon):
        complete_url = self.base_url +"lat=" + str(lat)+  "&lon=" + str(lon)+"&appid=" + self.api_key
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            country = data["sys"]["country"]
            city = data["name"]
            weather_desc = data["weather"][0]["description"]
            return main, weather_desc, country,city
        else:
            return None

if __name__ == "__main__":
    lat = os.getenv('LATITUDE')
    lon = os.getenv('LONGITUDE')
    weather_wrapper = WeatherWrapper()
    weather_info = weather_wrapper.get_weather(lat, lon)
    if weather_info:
        print("Country : ", weather_info[2])
        print("City : ", weather_info[3])
        print("Temperature : ", str(round(weather_info[0]["temp"] - 273.15, 2)))
        print("Weather description : ", str(weather_info[1]))
    else:
        print("Location not found!")
