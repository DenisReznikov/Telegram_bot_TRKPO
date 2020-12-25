import requests
import os



def search(type_of_place, longitude: float, latitude: float, range=0.223456, count = 3):
    try:
        YANDEX_TOKEN = "ca2c7dc4-1acc-4bbb-8785-d0ba647c2926"

        request = "https://search-maps.yandex.ru/v1/?text=" + type_of_place + "&ll=" + str(longitude) + "," + str(
            latitude) + "&spn="+str(range) + "," + str(range) + "&lang=en_EN&apikey=" + YANDEX_TOKEN
        data = requests.get(request)
        response = data.json()
        i = 0
        result = {}
        if response == "":
            return 1

        while i < count:
            place = type_of_place + ": " + response['features'][i]['properties']['name'] + "\n"

            addres = "Адресс:" + response['features'][i]['properties']['description'] + "\n"
            try:
                phone = "Телефон: " + response['features'][i]['properties']['CompanyMetaData']['Phones'][0]['formatted'] + "\n"
            except:
                phone = "Нет телефона"
            work_time = "Рабочее время " + response['features'][i]['properties']['CompanyMetaData']['Hours']['text']
            result[str(i) + 'longitude'] = response['features'][i]['geometry']['coordinates'][0]
            result[str(i) + 'latitude'] = response['features'][i]['geometry']['coordinates'][1]
            answer = addres + place + phone + work_time
            result[str(i) + 'answer'] = answer
            i += 1
        return result
    except Exception as e:
        print("Exception (yandex):", e)
        return 0
        pass