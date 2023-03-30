from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='authentication/change-password.html',
                                                                   success_url='/scrapping_app/home/'), name='change_password'),
    path('update-data/', views.update_user_info, name='update-data')
]
