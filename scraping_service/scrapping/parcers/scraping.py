import requests
import codecs
from bs4 import BeautifulSoup
from random import randint
import logging

__all__ = ('pracuj_scrap', 'pracuj_aplikujpl')

"""mask to be browser(firefox) while request"""
headers = [
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'},
]

errors = []


def pracuj_scrap(url):
    jobs = []
    domain = 'https://www.pracuj.pl'

    url_pracuj = url

    response = requests.get(url_pracuj, headers=headers[randint(0, 2)])
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            main_div = soup.find('div', attrs={'id': '__next'})
            div_list = main_div.find_all('div', attrs={'class': 'c8i823f'})
            for div in div_list:
                title_from_h2 = div.find('h2')
                title_conv = title_from_h2.text
                title_text_only = title_conv.strip().strip('"')
                # print(title_text_only)
                city_from_h5 = div.find('h5')
                city_conv = city_from_h5.text
                city_name_text_only = city_conv.strip().strip('"')
                # print(city_name_text_only)
                """getting direct link from href"""
                try:
                    href = title_from_h2.a['href']
                    # print(href)
                except TypeError:
                    logging.error('Url Error')

                companyName_from_h4 = div.find('h4')
                companyName_text_conv = companyName_from_h4.text
                companyName_text_only = companyName_text_conv.strip().strip('"')
                # print(f'{companyName_text_only}\n\n')
                try:
                    jobs.append({'title': title_text_only,
                                 'link': href,
                                 'company': companyName_text_only,
                                 'description': 'Test',
                                 'city': city_name_text_only,
                                 'language': 'Python',
                                 })
                except UnboundLocalError:
                    print('No data\n')

    except TypeError as e:
        errors.append({'Error': e})

    return jobs


def pracuj_aplikujpl(url):
    jobs = []
    domain = 'https://www.aplikuj.pl'
    url_aplikujpl = url

    response = requests.get(url_aplikujpl, headers=headers[randint(0, 2)])
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            main_div = soup.find('main', attrs={'id': 'page-content'})
            div_list = main_div.find_all('section', attrs={'class': 'max-w-6xl mx-auto'})
            for div in div_list:
                title_from_h3 = div.find('h3')
                title_conv = title_from_h3.text
                title_text_only = title_conv.strip().strip('"')
                # print(title_text_only)
                """getting direct link from href"""
                try:
                    href = title_from_h3.a['href']
                    logging.info(f'{domain}{href}')
                except TypeError:
                    logging.error('Url Error')
                city_from_div = div.find('span', attrs={'class': 'text-sm'})
                city_from_div_conv = city_from_div.text
                city_from_div_text = city_from_div_conv.strip().strip('"')
                company_name = div.find('div', attrs={'class': 'mt-1 text-sm'})
                company_name_conv = company_name.text
                company_name_conv_text_only = company_name_conv.strip().strip('"')
                company_name_final = company_name_conv_text_only.split()[0]
                jobs.append({'title': title_text_only,
                             'link': f'{domain}{href}',
                             'city': city_from_div_text,
                             'language': 'Python',
                             'description': 'Test',
                             'company': company_name_final,
                             })

    except TypeError as e:
        errors.append({'Error': e})

    return jobs


print(errors)
