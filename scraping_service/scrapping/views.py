from django.shortcuts import render
from django.views import View
from .models import Job_Offers
from .forms import FindForm
from django.core.paginator import Paginator
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        print(request.GET)
        form = FindForm()
        return render(request,
                      'scrapping/home.html',
                      {'form': form})


class ListView(View):
    def get(self, request):
        form = FindForm()
        city = request.GET.get('city')
        programming_language = request.GET.get('p_language')

        context = {'city': city, 'programming_language': programming_language, 'form': form}
        if city or programming_language:
            """Realization of filtering"""
            _filter = {}
            if city:
                _filter['city__name'] = city
            if programming_language:
                _filter['language__name'] = programming_language
            qs = Job_Offers.objects.filter(**_filter).order_by('-time_stamp')
            paginator = Paginator(qs, 10)

            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['object_list'] = page_obj
        return render(request,
                      'scrapping/list.html',
                      context)