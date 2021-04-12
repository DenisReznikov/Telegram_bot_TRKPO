[![unit test](https://github.com/DenisReznikov/Telegram_bot_TRKPO/actions/workflows/unit-test.yml/badge.svg)](https://github.com/DenisReznikov/Telegram_bot_TRKPO/actions/workflows/unit-test.yml)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Telegram  bot

## Description 
Bot shows bars, restaurants and cafes near you.\
Still bot helps to know the weather in any city or by your geolocation.\
Also helps to find the right thing on avito.

[@bot](https://t.me/trpko_70115_bot) You can test bot hear

### Requirements
* [Python](https://www.python.org) >= 3.5(64bit)
* [beautifulsoup4](https://github.com/wention/BeautifulSoup4) and [lxml](https://github.com/lxml/lxml) library for pulling data out of HTML (avito)  
* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) - library provides a pure Python interface for the Telegram Bot API
* [requests](https://github.com/psf/requests) - library allows you to send HTTP requests
 ### Installing  
    > git clone https://github.com/DenisReznikov/Telegram_bot_TRKPO.git
    > pip install -r requirements.txt
    > python main.py
    
### Application architecture
```
telegrambot/
├── scr/ 
|   ├── model/                    // model (work with weather and Yandex.Map API and parsing Avito)
|   ├── handler/                   // connect model and telegram API
```
