from django.contrib import admin
from .models import City, Programming_Language, Job_Offers
# Register your models here.

admin.site.register(City)
admin.site.register(Programming_Language)
admin.site.register(Job_Offers)