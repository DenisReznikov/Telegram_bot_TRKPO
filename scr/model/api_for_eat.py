import requests
import os



def search(type_of_place, longitude: float, latitude: float, range: float):
    try:
        YANDEX_TOKEN = "ca2c7dc4-1acc-4bbb-8785-d0ba647c2926"
        if range == "":
            range = 0.223456
        request = "https://search-maps.yandex.ru/v1/?text=" + type_of_place + "&ll=" + str(longitude) + "," + str(
            latitude) + "&spn="+str(range) + "," + str(range) + "&lang=en_EN&apikey=" + YANDEX_TOKEN
        data = requests.get(request)
        response = data.json()
        i = 0
        result = {}
        while i < 3:
            answer = type_of_place + ": " + response['features'][i]['properties']['name'] + "\n" \
                     + "Address:" + response['features'][i]['properties']['description'] + "\n" \
                     + "Phone: " + response['features'][i]['properties']['CompanyMetaData']['Phones'][0][
                         'formatted'] + "\n" \
                     + "Work time " + response['features'][i]['properties']['CompanyMetaData']['Hours']['text']
            result[str(i) + 'longitude'] = response['features'][i]['geometry']['coordinates'][0]
            result[str(i) + 'latitude'] = response['features'][i]['geometry']['coordinates'][1]
            result[str(i) + 'answer'] = answer
            i += 1
        return result
    except Exception as e:
        print("Exception (yandex):", e)
        return "Something go wrong"
        pass