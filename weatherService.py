import os, requests
from WeatherData import WeatherData
from dotenv import load_dotenv

load_dotenv()


def getWeatherFromLocationName(location: str):
    API_KEY = os.getenv("API_KEY")
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": location, "days": "1"}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    resp = response.json()

    WeatherDataObj = WeatherData(
        resp["location"]["name"],
        resp["location"]["country"],
        resp["location"]["lat"],
        resp["location"]["lon"],
        resp["current"]["temp_c"],
    )
    return WeatherDataObj
