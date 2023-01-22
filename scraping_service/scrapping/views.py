from django.shortcuts import render
from .models import Job_Offers
# Create your views here.


def home_view(request):
    qs = Job_Offers.objects.all()
    context = {'object_list': qs}
    return render(request, 'scrapping/home.html', context)