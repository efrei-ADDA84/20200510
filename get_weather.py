from sanic import Sanic, response
import os
import requests

app = Sanic("get_weather")

class WeatherWrapper:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')  
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self, lat, lon):
        complete_url = self.base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + self.api_key
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            country = data["sys"]["country"]
            city = data["name"]
            weather_desc = data["weather"][0]["description"]
            return main, weather_desc, country, city
        else:
            return None

@app.route("/")
async def get_weather_info(request):
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        return response.json({"error": "Latitude and longitude are required."}, status=400)

    weather_wrapper = WeatherWrapper()
    weather_info = weather_wrapper.get_weather(lat, lon)

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
    app.run(host="0.0.0.0", port=8081)
