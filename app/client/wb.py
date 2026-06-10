from curl_cffi import requests

from app.config import settings

session = requests.Session(impersonate="chrome120")
session.headers.update({'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive",
                        "Host": "www.wildberries.ru",
                        "Pragma": "no-cache",
                        "Priority": "u=0, i",
                        "Referer": "https://www.google.com/",
                        "Sec-Fetch-Dest": "document",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-Site": "cross-site",
                        "TE": "trailers",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:151.0) Gecko/20100101 Firefox/151.0"})
session.cookies.update(settings.cookie_wb)


def get_wb_product_data(article):
    url = "https://www.wildberries.ru/__internal/u-card/cards/v4/detail"

    params = {
        "nm": int(article),
        "appType": "1",
        "curr": "rub",
        "lang": "ru",
        "dest": "1259570991"
    }
    try:
        response = session.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()
            product = result['products'][0]
            name = product["name"]
            price_kopecks = product['sizes'][0]['price']['product']
            price_rub = price_kopecks / 100
            return price_rub, name
        else:
            print("Отправляем письмо хозяину")
    except (KeyError, IndexError) as ex:
        print("Отправляем письмо хозяину")
        return (0, "Ошибка парсинга")
    except (requests.RequestsError, ConnectionError, TimeoutError) as ex:
        print("Отправляем письмо хозяину")
        return (0, "Ошибка парсинга")