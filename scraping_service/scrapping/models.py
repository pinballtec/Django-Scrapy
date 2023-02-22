from django.db import models
from .utils import from_cyrillic_to_eng


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='City Name', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'City collection'


class Programming_Language(models.Model):
    name = models.CharField(max_length=10, verbose_name="Programming Language")
    slug = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Programming language collection'


class Job_Offers(models.Model):
    urls = models.URLField(max_length=200, unique=True)
    title = models.CharField(max_length=30, verbose_name='Name of job offer')
    company = models.CharField(max_length=15,
                               verbose_name='Name of the company')
    description = models.TextField(
        verbose_name='Job description of the vacancy')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Programming_Language,
                                 on_delete=models.CASCADE,
                                 null=True)

    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Job offers collection model'

    def __str__(self):
        return self.title
