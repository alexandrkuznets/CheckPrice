from curl_cffi import requests

from app.config import settings
from app.celery_app import logger
from app.services.email import send_email_to_host

session = requests.Session(impersonate="chrome120")
session.headers.update({
"Accept": "*/*",
"Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"deviceid": "site_c0f729feace542a6ade803f312edc6d9",
"Host": "www.wildberries.ru",
"Pragma": "o-cache",
"Priority": "u=4",
"Referer": "https://www.wildberries.ru/",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"TE": "trailers",
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0",
"x-requested-with": "XMLHttpRequest",
"x-spa-version": "14.16.1"
})
session.cookies.update(settings.cookie_wb)


def get_wb_product_data(article):
    url = "https://www.wildberries.ru/__internal/u-card/cards/v4/detail"


    params = {
        "nm": int(article),
        "appType": "1",
        "curr": "rub",
        "lang": "ru",
        "dest": "-1257786",
        "ab_testing": "false",
        "mtype": "257",
        "hide_dtype": "15",
        "hide_vflags": "4294967296",
        "spp": "30"
    }
    try:
        response = session.get(
            url,
            params=params,
            timeout=10
        )
        if response.status_code == 200:
            logger.info("Успешный запрос! status_code: 200")
            result = response.json()
            product = result['products'][0]
            name = product["name"]
            price_kopecks = product['sizes'][0]['price']['product']
            price_rub = price_kopecks / 100
            return price_rub, name
        else:
            logger.warning(f"Результат запроса к WB: {response.status_code}")
            send_email_to_host(f"Статус код ответа: {response.status_code}")
            return (0, "Ошибка парсинга")
    except (KeyError, IndexError) as ex:
        logger.error(f"Результат запроса к WB: Ошибка {ex}")
        send_email_to_host(f"{ex}")
        return (0, "Ошибка парсинга")
    except (requests.RequestsError, ConnectionError, TimeoutError) as ex:
        logger.error(f"Результат запроса к WB: Ошибка {ex}")
        send_email_to_host(f"{ex}")
        return (0, "Ошибка парсинга")