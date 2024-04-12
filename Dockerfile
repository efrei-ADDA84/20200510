FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# ENV OPENWEATHER_API_KEY='303cc60b4908b33b88f1dfa22fc51ed9'
# ENV LATITUDE=30
# ENV LONGITUDE=20

CMD ["python", "get_weather.py"]
