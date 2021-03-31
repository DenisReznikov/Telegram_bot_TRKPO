import datetime
import urllib.parse
from collections import namedtuple

import bs4
import requests

InnerBlock = namedtuple('Block', 'title,price,currency,date,url')


class Block(InnerBlock):
    def __str__(self):
        return f'{self.title}\nЦена: {self.price} {self.currency} \nДата размещения: {self.date}\nСсылка: {self.url}'


class AvitoParser:
    def __init__(self, metro, object_for_search, sort_type):
        self.metro = metro
        self.sort_type = sort_type
        self.object_for_search = object_for_search
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                          'Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }

    def get_page(self, page: int = None):
        params = {
            'radius': 0,
            'user': 1,
        }
        if page and page > 1:
            params['p'] = page

        url = f'https://www.avito.ru/sankt-peterburg?metro={self.metro}&q={self.object_for_search}&s={self.sort_type}'
        print(url)
        r = self.session.get(url, params=params)
        return r.text


    def parse_block(self, item):
        # Выбрать блок со ссылкой
        url_block = item.select_one('a.link-link-39EVK.link-design-default-2sPEv.title-root-395AQ.iva-item-title-1Rmmj.title-list-1IIB_.title-root_maxHeight-3obWc')
        href = url_block.get('href')

        if href:
            url = 'https://www.avito.ru' + href
        else:
            url = None

        # Выбрать блок с названием
        title_block = item.select_one('div.iva-item-titleStep-2bjuh')
        title = title_block.text.strip()

        # Выбрать блок с названием и валютой
        price_block = item.select_one('span.price-text-1HrJ_.text-text-1PdBw.text-size-s-1PUdo')
        price_block = price_block.get_text('\n')
        price_block = list(filter(None, map(lambda i: i.strip(), price_block.split('\n'))))
        if len(price_block) == 2:
            price, currency = price_block
        elif len(price_block) == 1:
            # Бесплатно
            price, currency = 0, None
        else:
            price, currency = None, None
            print(f'Что-то пошло не так при поиске цены: {price_block}, {url}')

        # Выбрать блок с датой размещения объявления
        date = None
        date_block = item.select_one('div.date-text-2jSvU.text-text-1PdBw.text-size-s-1PUdo.text-color-noaccent-bzEdI')

        absolute_date = date_block.get_text()


        return Block(
            url=url,
            title=title,
            price=price,
            currency=currency,
            date=absolute_date,
        )

    def get_pagination_limit(self):
        text = self.get_page()
        soup = bs4.BeautifulSoup(text, 'lxml')

        container = soup.select('a.pagination-page')
        last_button = container[-1]
        href = last_button.get('href')
        if not href:
            return 1

        r = urllib.parse.urlparse(href)
        params = urllib.parse.parse_qs(r.query)
        return int(params['p'][0])

    def get_blocks(self, page: int = 1):
        
        text = self.get_page(page=page)
        soup = bs4.BeautifulSoup(text, 'lxml')
        print(text)
        print("--------------")
        print(soup)
        # Запрос CSS-селектора, состоящего из множества классов, производится через select
        container = soup.select('div.iva-item-root-G3n7v.photo-slider-slider-3tEix.iva-item-list-2_PpT.items-item-1Hoqq.items-listItem-11orH.js-catalog-item-enum')
        array_for_block = []
        print(len(container))
        for item in container:
            block = self.parse_block(item=item)
            array_for_block.append(block)
        return array_for_block
