from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scrapping_app/', include('scrapping.urls')),
    path('authentication/', include('authentication.urls'))
]
