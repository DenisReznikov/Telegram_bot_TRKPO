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
        print("Exception (forecast):", e)
        return "Что-то пошло не так"
        pass


def get_wind_direction(deg):
    compass_point = [' N ', 'NE ', ' E ', 'SE ', ' S ', 'SW ', ' W ', 'NW ']
    res = ""
    for i in range(0, 8):
        step = 45.
        min = i * step - 45 / 2.
        max = i * step + 45 / 2.
        if i == 0 and deg > 360 - 45 / 2.:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = compass_point[i]
            break
    return res

def request_forecast(city_name="", lon=0, lat=0):
    try:
        WEATHER_TOKEN = "0b9d7aa6e6a02a716eb58669c60f0ccf"
        if "" == city_name:
            res = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                               params={'lat': str(lat), 'lon': str(lon), 'units': 'metric', 'lang': 'en',
                                       'APPID': WEATHER_TOKEN})
        else:
            res = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                               params={'q': city_name, 'units': 'metric', 'lang': 'en', 'APPID': WEATHER_TOKEN})
        data = res.json()
        answer = ''
        for i in data['list']:
            answer += str((i['dt_txt'])[:16] + '{0:+3.0f}'.format(i['main']['temp']) + " °C"
                                                                                       '{0:2.0f}'.format(i['wind']['speed']) + " m/s  " +
                          "direction of the wind: " + get_wind_direction(i['wind']['deg']) + " " +
                          i['weather'][0]['description']) + "\n"
        return answer
    except Exception as e:
        print("Exception (forecast):", e)
        return "Что-то пошло не так"
        pass