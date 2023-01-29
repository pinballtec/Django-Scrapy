from django.shortcuts import render
from django.views import View
from .models import Job_Offers
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        qs = Job_Offers.objects.all()
        context = {'object_list': qs}
        return render(request, 'scrapping/home.html', context)