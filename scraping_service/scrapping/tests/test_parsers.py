import unittest
from ..parcers import scraping


class TestPracujScrap(unittest.TestCase):

    def test_pracuj_scrap(self):
        url = 'https://www.pracuj.pl/praca/programista%20python;kw?et=17%2C1'
        jobs = scraping.pracuj_scrap(url)

        # Check that the jobs list is not empty
        self.assertTrue(jobs)

        # Check that each job has a title, link, company, description, city, and language
        for job in jobs:
            self.assertIn('title', job)
            self.assertIn('link', job)
            self.assertIn('company', job)
            self.assertIn('description', job)
            self.assertIn('city', job)
            self.assertIn('language', job)

            # Check that the title is a non-empty string
            self.assertIsInstance(job['title'], str)
            self.assertTrue(job['title'])

            # Check that the link is a non-empty string
            self.assertIsInstance(job['link'], str)
            self.assertTrue(job['link'])

            # Check that the company is a non-empty string
            self.assertIsInstance(job['company'], str)
            self.assertTrue(job['company'])

            # Check that the description is a non-empty string
            self.assertIsInstance(job['description'], str)
            self.assertTrue(job['description'])

            # Check that the city is a non-empty string
            self.assertIsInstance(job['city'], str)
            self.assertTrue(job['city'])

            # Check that the language is a non-empty string
            self.assertIsInstance(job['language'], str)
            self.assertTrue(job['language'])

    def setUp(self):
        self.url = 'https://www.aplikuj.pl/praca/zawod/python-developer'

    def test_pracuj_aplikujpl(self):
        jobs = scraping.pracuj_aplikujpl(self.url)
        self.assertTrue(len(jobs) > 0)
        for job in jobs:
            self.assertIn('title', job)
            self.assertIn('link', job)
            self.assertIn('city', job)
            self.assertIn('language', job)
            self.assertIn('description', job)
            self.assertIn('company', job)