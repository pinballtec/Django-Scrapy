from scrapping.parcers.scraping import *
import codecs

parsers = ((pracuj_scrap, 'https://www.pracuj.pl/praca/programista%20python;kw?et=17%2C1'),
           (pracuj_aplikujpl, 'https://www.aplikuj.pl/praca/zawod/python-developer'))

jobs, errors = [], []
for func, url in parsers:
    j = func(url)
    jobs += j

