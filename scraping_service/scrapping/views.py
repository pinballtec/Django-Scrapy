from django.shortcuts import render
from django.views import View
from .models import Job_Offers
from .forms import FindForm
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        print(request.GET)
        form = FindForm()
        city = request.GET.get('city')
        programming_language = request.GET.get('p_language')
        qs = []
        if city or programming_language:
            """Realization of filtering"""
            _filter = {}
            if city:
                _filter['city__name'] = city
            if programming_language:
                _filter['language__name'] = programming_language
            qs = Job_Offers.objects.filter(**_filter)
        return render(request, 'scrapping/home.html', {'object_list': qs, 'form': form})