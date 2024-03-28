import os
import requests
import json

class WeatherWrapper:
    def __init__(self):
        self.api_key = '303cc60b4908b33b88f1dfa22fc51ed9'
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
    lat = '34.003342'
    lon = '-118.485832'
    weather_wrapper = WeatherWrapper()
    weather_info = weather_wrapper.get_weather(lat, lon)
    if weather_info:
        print("Country : " + weather_info[2] + "\nCity : " + weather_info[3] + "\nTemperature : " +
                        str(round(weather_info[0]["temp"] - 273.15, 2)) +
              "\nWeather description : " +
                        str(weather_info[1]))
    else:
        print("Location not found!")
