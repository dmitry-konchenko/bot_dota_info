import requests
from bs4 import BeautifulSoup


def get_meta(position: str) -> list[tuple[str, str]]:
    meta_html_elements = ''
    meta_list = []
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Charset': 'UTF-8',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': '_tz=Europe%2FMoscow; _hi=1680351575503',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    response = requests.get(f'https://www.dota2protracker.com/meta', headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    if position.lower() == 'carry':
        meta_html_elements = soup.select('.content-box.tabs-2')[0]
    elif position.lower() == 'mid':
        meta_html_elements = soup.select('.content-box.tabs-3')[0]
    elif position.lower() == 'offlane':
        meta_html_elements = soup.select('.content-box.tabs-4')[0]
    elif position.lower() == 'hardsup':
        meta_html_elements = soup.select('.content-box.tabs-5')[0]
    elif position.lower() == 'fullsup':
        meta_html_elements = soup.select('.content-box.tabs-6')[0]
    meta_names = meta_html_elements.select('.top-hero-head a')
    meta_win_rates = meta_html_elements.select('.green.all-wr')
    for i in range(len(meta_names)):
        meta_tuple = meta_names[i]['title'], meta_win_rates[i].text
        meta_list.append(meta_tuple)
    return meta_list

