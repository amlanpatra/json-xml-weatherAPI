from fastapi import FastAPI, Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from weatherService import getWeatherFromLocationName

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.post("/getCurrentWeather")
async def getCurrentWeather(request: Request):
    try:
        data = await request.json()
        city = data[0]["city"]
        output_format = data[0]["output_format"]

        weatherDataObj = getWeatherFromLocationName(city)

        if output_format == "json":
            return weatherDataObj.to_json()
        else:
            return weatherDataObj.to_xml()

    except Exception as e:
        print("error", e)


uvicorn.run(app, host="0.0.0.0", port=8080)  # type: ignore
