import datetime

import requests


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

    @staticmethod
    def parse_date(item):
        params = item.strip().split(' ')
        # print(params)
        if len(params) == 2:
            day, time = params
            if day == 'Сегодня':
                date = datetime.date.today()
            elif day == 'Вчера':
                date = datetime.date.today() - datetime.timedelta(days=1)
            else:
                print('Не смогли разобрать день:', item)
                return

            time = datetime.datetime.strptime(time, '%H:%M').time()
            return datetime.datetime.combine(date=date, time=time)

        elif len(params) == 3:
            day, month_hru, time = params
            day = int(day)
            months_map = {
                'января': 1,
                'февраля': 2,
                'марта': 3,
                'апреля': 4,
                'мая': 5,
                'июня': 6,
                'июля': 7,
                'августа': 8,
                'сентября': 9,
                'октября': 10,
                'ноября': 11,
                'декабря': 12,
            }
            month = months_map.get(month_hru)
            if not month:
                print('Не смогли разобрать месяц:', item)
                return

            today = datetime.datetime.today()
            time = datetime.datetime.strptime(time, '%H:%M')
            return datetime.datetime(day=day, month=month, year=today.year, hour=time.hour, minute=time.minute)

        else:
            print('Не смогли разобрать формат:', item)
            return
