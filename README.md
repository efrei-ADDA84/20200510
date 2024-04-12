# 20200510

TP1 : 

Run docker : docker run -it --rm --name running_weather_app -e OPENWEATHER_API_KEY=your_api_key -e LATITUDE=your_latitude -e LONGITUDE=your_longitude my_weather_app


DockerHub link : https://hub.docker.com/repository/docker/nassim933/tp1/general

Rapport: 

J'ai utilisé python car c'est le langage que je précise le plus. A part pour la configuration de Docker et d'avoir le bon lien pour l'utilisation de l'API, j'ai pas rencontré d'autre difficultés . 


TP2 : 

link API : http://localhost:8000/get_weather

body JSON : 
{
    "latitude" : "your_latitude",
    "longitude" : "your_longitude",
    "api_key" : "your API KEY"
}