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