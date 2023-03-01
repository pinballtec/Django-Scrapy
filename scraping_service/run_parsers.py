import django
import os
import sys
import logging

from django.contrib.auth import get_user_model
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)

os.environ["DJANGO_SETTINGS_MODULE"] = 'scraping_service.settings'
django.setup()

from scrapping.models import City, Programming_Language, Job_Offers, Errors
from scrapping.parcers.scraping import *

user = get_user_model()

parsers = ((pracuj_aplikujpl, 'https://www.aplikuj.pl/praca/zawod/python-developer'),
           (pracuj_scrap, 'https://www.pracuj.pl/praca/programista%20python;kw?et=17%2C1'))


def get_settings():
    """getting info from user saving in newsletter"""
    qs = user.objects.filter(newsletter=True).values()
    settings_list = set((q['city_id'], q['language_id']) for q in qs)
    return settings_list


city = City.objects.filter(slug='kiev').first()
language = Programming_Language.objects.filter(slug='teSt').first()

jobs, errors = [], []
for func, url in parsers:
    try:
        j, e = func(url)
        jobs += j
        errors += e
    except ValueError:
        logging.error("Error stack is failed")
    finally:
        j = func(url)
        jobs += j

for parser, url in parsers:
    jobs = parser(url)
    for job in jobs:
        city, _ = City.objects.get_or_create(name=job['city'])
        language, _ = Programming_Language.objects.get_or_create(name=job['language'])
        job_offer, created = Job_Offers.objects.get_or_create(urls=job['link'])
        if not created:
            job_offer.title = job['title']
            job_offer.company = job['company']
            job_offer.description = job['description']
            job_offer.city = city
            job_offer.language = language
            job_offer.save()
            logging.info("Job offer updated successfully")
        else:
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

    if errors:
        er = Errors(data=errors).save()

print(logging.getLogger('scrapping').getEffectiveLevel())
