import requests
import json


API_KEY = "c0707899522e006c1e78c0bfba58ced1"
city_name = input("Enter city name: ")
URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

res = requests.get(URL)
json_data = json.loads(res.text)
weather = json_data["weather"][0]["description"]
temprature = json_data["main"]["temp"]
humidity = json_data["main"]["humidity"]
wind_speed = json_data["wind"]["speed"]

print(f"weagter: {weather}")
print(f"temprature: {temprature}")
print(f"humidity: {humidity}")
print(f"wind_speed: {wind_speed}")