from django.urls import path
from .views import HomeView, ListView

urlpatterns = [
    path('list/', ListView.as_view(), name='list'),
    path('home/', HomeView.as_view(), name='home')
]

