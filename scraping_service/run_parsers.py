import django
import os
import sys
import logging

from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)

os.environ["DJANGO_SETTINGS_MODULE"] = 'scraping_service.settings'
django.setup()

from scrapping.models import City, Programming_Language, Job_Offers
from scrapping.parcers.scraping import *

parsers = ((pracuj_aplikujpl, 'https://www.aplikuj.pl/praca/zawod/python-developer'),
           (pracuj_aplikujpl, 'https://www.aplikuj.pl/praca/zawod/python-developer'))

city = City.objects.filter(slug='kiev').first()
language = Programming_Language.objects.filter(slug='teSt').first()

jobs = []
for func, url in parsers:
    j = func(url)
    jobs += j

# print(jobs)
e = 0
for parser, url in parsers:
    jobs = parser(url)
    for job in jobs:
        city, _ = City.objects.get_or_create(name=job['city'])
        language, _ = Programming_Language.objects.get_or_create(name=job['language'])
        job_offer = Job_Offers(
            urls=job['link'],
            title=job['title'],
            company=job['company'],
            description=job['description'],
            city=city,
            language=language
        )
        try:
            job_offer.save()
        except DatabaseError as e:
            logging.error(f"Error saving job offer: {e}")
        else:
            logging.info("Job offer saved successfully")

