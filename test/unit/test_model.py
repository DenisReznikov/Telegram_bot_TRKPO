from scr.model.api_for_weather import get_wind_direction, request_current_weather, request_forecast
from scr.model.api_for_eat import search
from scr.model.avito_model import Block, AvitoParser
import requests
from bs4 import BeautifulSoup


def test_get_wind_direction_pos():
    deg = 10
    response = get_wind_direction(deg)
    direction = 'N'
    assert (response.replace(' ', '')) == direction


def test_get_wind_direction_neg():
    deg = 10
    response = get_wind_direction(deg)
    direction = 'NE'
    assert (response.replace(' ', '')) != direction


def test_request_forecast_pos():
    bad_response = 'Что-то пошло не так'
    response = request_forecast(city_name="", lon=0, lat=0)
    assert response != bad_response


def test_request_forecast_neg():
    bad_response = 'Что-то пошло не так'
    response = request_forecast(city_name="Badbsgfsds", lon=1110, lat=1110)
    assert response == bad_response


def test_request_current_weather_pos():
    bad_response = 'Что-то пошло не так'
    response = request_current_weather(city_name="", lon=0, lat=0)
    assert response != bad_response


def test_request_current_weather_neg():
    bad_response = 'Что-то пошло не так'
    response = request_current_weather(city_name="DFQfdf", lon=12309, lat=123009)
    assert response == bad_response


def test_search_pos():
    result = search('Кафе',  30.354011, 59.983283, range=1.223456, count=3)
    expected_response = {'0longitude': 30.352474, '0latitude': 59.98324}
    assert str(expected_response['0longitude']) == str(result['0longitude'])


def test_search_neg():
    result = search('Р',  30.354011, 59.983283, range=1.223456, count=3)
    expected_response = 0
    assert str(expected_response) == str(result)


def test_get_page():
    parser = AvitoParser(metro='159',
                         object_for_search='Naruto',
                         sort_type='1')
    soup1 = BeautifulSoup(parser.get_page(1), 'lxml')
    product_name_parts1 = soup1.find('h3', class_='title-root-395AQ iva-item-title-1Rmmj title-list-1IIB_ title-root_maxHeight-3obWc text-text-1PdBw text-size-s-1PUdo text-bold-3R9dt').text
    response = requests.get('https://www.avito.ru/sankt-peterburg?metro=159&q=%D0%9D%D0%B0%D1%80%D1%83%D1%82%D0%BE&s=1')
    soup2 = BeautifulSoup(response.text, 'lxml')
    product_name_parts2 = soup2.find('h3', class_='title-root-395AQ iva-item-title-1Rmmj title-list-1IIB_ title-root_maxHeight-3obWc text-text-1PdBw text-size-s-1PUdo text-bold-3R9dt').text
    assert product_name_parts1 == product_name_parts2


def test_get_blocks():
    parser = AvitoParser(metro='159',
                         object_for_search='Naruto',
                         sort_type='1')
    result = parser.get_blocks()
    response = requests.get('https://www.avito.ru/sankt-peterburg?metro=159&q=%D0%9D%D0%B0%D1%80%D1%83%D1%82%D0%BE&s=1')
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.select(
        'div.iva-item-root-G3n7v.photo-slider-slider-3tEix.iva-item-list-2_PpT.items-item-1Hoqq.items-listItem-11orH.js-catalog-item-enum')
    array_for_block = []
    for item in container:
        block = parser.parse_block(item=item)
        array_for_block.append(block)
    assert result[1] == array_for_block[1]


def test_get_pagination_limit_neg():
    parser = AvitoParser(metro='159',
                         object_for_search='Naruto',
                         sort_type='1')
    result = parser.get_pagination_limit()
    assert result == 1


#def test_parse_block():
#    parser = AvitoParser(metro='159',
#                         object_for_search='Naruto',
#                         sort_type='1')
#
#    result = parser.parse_block()
#   time.sleep(15)
#   response = requests.get('https://www.avito.ru/sankt-peterburg?metro=159&q=BMW&s=1')
#   soup = BeautifulSoup(response.text, 'lxml')
#   container = soup.select('a.pagination-page')
#   last_button = container[-1]
#   href = last_button.get('href')
#   r = urllib.parse.urlparse(href)
#   params = urllib.parse.parse_qs(r.query)
