import requests
import codecs
from bs4 import BeautifulSoup
from random import randint

"""mask to be browser(firefox) while request"""
headers = [
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'},
]


def pracuj_aplikujpl(url):
    jobs = []
    errors = []
    domain = 'https://www.aplikuj.pl'
    url_aplikujpl = url

    response = requests.get(url_aplikujpl, headers=headers[randint(0, 2)])
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            main_div = soup.find('main', attrs={'id': 'page-content'})
            div_list = main_div.find_all('section', attrs={'class': 'max-w-6xl mx-auto'})
            for i in div_list:
                city_from_div = i.find('span', attrs={'class': 'text-sm'})
                company_name = i.find('div', attrs={'class': 'mt-1 text-sm'})
                title_conv = company_name.text
                title_text_only = title_conv.strip().strip('"')
                text = title_text_only.split()[0]
                print(title_text_only)
            e = 0
    except TypeError as e:
        errors.append(e)


print(
    pracuj_aplikujpl(
        'https://www.aplikuj.pl/praca/zawod/python-developer'
    )
)