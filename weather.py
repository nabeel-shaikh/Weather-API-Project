import requests
api_key = "3faca67aaf2a1deacc9f8876f1da3dc0"
url = "http://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")

requests_url = f"{url}?appid={api_key}&q={city}" #fetch data from website
requested_data = requests.get(requests_url)
if requested_data.status_code == 200: #means the city name was valid and data has been fetched
    data = requested_data.json()
    temp = round((int(data["main"]['temp']))-273.15)
    feels_like = round(int(data["main"]['feels_like'])-273.15)
    wind = round(int(data["wind"]['speed'])*18/5)
    weather_desc = data["weather"][0]["description"]
    hpa = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    print("Weather: {}.".format(weather_desc))
    print("Temperature: {} degrees.".format(temp))
    print("Feels like: {} degrees.".format((feels_like)))
    print("Wind speed: {} km/h".format(wind))
    print("Humidity: {}%.".format(humidity))
    print("Pressure: {} hPa.".format(hpa))
else:
    print("An error has occured!")
