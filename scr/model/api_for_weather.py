import requests

def request_current_weather(city_name="", lon=0, lat=0):
    try:
        WEATHER_TOKEN = "0b9d7aa6e6a02a716eb58669c60f0ccf"
        if city_name == "":
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'lat': str(lat), 'lon': str(lon), 'units': 'metric', 'lang': 'en',
                                       'APPID': WEATHER_TOKEN})
        else:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'q': city_name, 'units': 'metric', 'lang': 'en', 'APPID': WEATHER_TOKEN})
        data = res.json()
        answer = ''
        answer += "conditions:  " + str(data['weather'][0]['description']) + '\n'
        answer += "temp:        " + str(data['main']['temp']) + '°C' + '\n'
        answer += "temp_min:    " + str(data['main']['temp_min']) + '°C' + '\n'
        answer += "temp_max:    " + str(data['main']['temp_max']) + '°C' + '\n'
        return answer
    except Exception as e:
        print("Exception (weather):", e)
        return 'Something go wrong'
        pass