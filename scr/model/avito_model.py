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
