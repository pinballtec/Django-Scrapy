from django.db import models
from .utils import from_cyrillic_to_eng


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='City Name')
    slug = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Programming_Language(models.Model):
    name = models.CharField(max_length=10, verbose_name="Programming Language")
    slug = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Job_Offers(models.Model):
    urls = models.URLField(max_length=200)
    title = models.CharField(max_length=30, verbose_name='Name od job offer')
    company = models.CharField(max_length=15, verbose_name='Name of the company')
    description = models.TextField(verbose_name='Job description of the vacancy')
    City = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    Language = models.ForeignKey(Programming_Language, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
