import requests
from bs4 import BeautifulSoup


def get_counterpick_function(hero_name: str) -> list[str]:
    request_hero_name = '-'.join(hero_name.lower().split())
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': '_tz=Europe%2FMoscow; _hi=1680351575503',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    response = requests.get(f'https://ru.dotabuff.com/heroes/{request_hero_name}/counters', headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    counter_html_elements = soup.select('.col-6:nth-child(1) .counter-outline td:nth-child(2)')
    counter_list = [line.text for line in counter_html_elements]
    return counter_list
