import requests
import codecs
from bs4 import BeautifulSoup
from random import randint

__all__ = ('pracuj_scrap', 'pracuj_aplikujpl')

"""mask to be browser(firefox) while request"""
headers = [
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'},
]

errors = []
jobs = []


def pracuj_scrap(url):
    domain = 'https://www.pracuj.pl'

    url_pracuj = url

    response = requests.get(url_pracuj, headers=headers[randint(0, 2)])
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            main_div = soup.find('div', attrs={'id': '__next'})
            div_list = main_div.find_all('div', attrs={'class': 'c1dwhfs6'})
            # print(div_list)
            for div in div_list:
                title_from_h2 = div.find('h2')
                title_conv = title_from_h2.text
                title_text_only = title_conv.strip().strip('"')
                print(title_text_only)
                """getting direct link from href"""
                try:
                    href = title_from_h2.a['href']
                    print(href)
                except TypeError:
                    print('Error with link, try smth else')

                companyName_from_h4 = div.find('h4')
                companyName_text_conv = companyName_from_h4.text
                companyName_text_only = companyName_text_conv.strip().strip('"')
                print(f'{companyName_text_only}\n\n')
                jobs.append({'Title': title_text_only,
                             'link': href,
                             'CompanyName': companyName_text_only
                             })
        # else:
        #     errors.append()

    except TypeError as e:
        errors.append(e)

    # print(jobs)
    return response


def pracuj_aplikujpl(url):
    domain = 'https://www.aplikuj.pl'
    url_olx = url

    response = requests.get(url_olx, headers=headers[randint(0, 2)])
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            main_div = soup.find('main', attrs={'id': 'page-content'})
            div_list = main_div.find_all('section', attrs={'class': 'max-w-6xl mx-auto'})
            # print(div_list)
            for div in div_list:
                title_from_h3 = div.find('h3')
                title_conv = title_from_h3.text
                title_text_only = title_conv.strip().strip('"')
                print(title_text_only)
                """getting direct link from href"""
                try:
                    href = title_from_h3.a['href']
                    print(f'{domain}{href}')
                except TypeError:
                    print('Error with link, try smth else')

                companyName_from_h4 = div.find('h4')
                companyName_text_conv = companyName_from_h4.text
                companyName_text_only = companyName_text_conv.strip().strip('"')
                print(f'{companyName_text_only}\n\n')
                jobs.append({'Title': title_text_only,
                             'link': f'{domain}{href}',
                             'CompanyName': companyName_text_only
                             })
        # else:
        #     errors.append()

    except TypeError as e:
        errors.append(e)

    # print(jobs)
    return response


# print(
#     pracuj_scrap(
#         'https://www.pracuj.pl/praca/programista%20python;kw?et=17%2C1'
#     )
# )
# print(
#     pracuj_aplikujpl(
#         'https://www.aplikuj.pl/praca/zawod/python-developer'
#     )
# )
#
# print(jobs)

# h = codecs.open('work.txt', 'w', 'utf8')
# h.write(str(jobs))
# h.close()

# if __name__ == '__main__':
#     url = 'https://www.pracuj.pl/praca/programista%20python;kw?et=17%2C1'
#     jobs, errors = pracuj_scrap(url)
#     h = codecs.open('work.txt', 'w', 'utf-8')
#     h.write(str(jobs))
#     h.close()

