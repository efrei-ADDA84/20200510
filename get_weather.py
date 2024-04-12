import os
import requests
from sanic import Sanic, response
from sanic.exceptions import SanicException

app = Sanic('get_weather')

class WeatherWrapper:
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self, lat, lon, api_key):
        complete_url = self.base_url +"lat=" + str(lat)+  "&lon=" + str(lon)+"&appid=" + str(api_key)
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
        


@app.route("/get_weather", methods=['POST'])
async def main(request):
    data = request.json
    if not data.get('latitude'):
        raise SanicException("'latitude' are necessary", status_code = 500)
    if not data.get('longitude'):
        raise SanicException("'longitude' are necessary", status_code = 501)
    if not data.get('api_key'):
        raise SanicException("'api_key' are necessary", status_code = 502)
    lat = data.get('latitude')
    lon = data.get('longitude')
    api_key = data.get('api_key')
    weather_wrapper = WeatherWrapper()
    weather_info = weather_wrapper.get_weather(lat, lon, api_key)
    if weather_info:
        temperature = round(weather_info[0]["temp"] - 273.15, 2)
        weather_description = weather_info[1]
        country = weather_info[2]
        city = weather_info[3]
        return response.json({
            "country": country,
            "city": city,
            "temperature": temperature,
            "weather_description": weather_description
        })
    else:
        return response.json({"error": "Location not found!"}, status=404)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
