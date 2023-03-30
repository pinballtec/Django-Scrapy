from django.shortcuts import render, redirect
from .forms import NewUserForm, UserLoginForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Account has been created, you can log in')
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_page(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'authentication/login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('login')


def update_user_info(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():
                user.city = form.cleaned_data['city']
                user.language = form.cleaned_data['language']
                user.newsletter = form.cleaned_data['newsletter']
                user.save()
                return redirect('home')
        else:
            form = UserUpdateForm(initial={'city': user.city,
                                           'language': user.language,
                                           'newsletter': user.newsletter})
        return render(request, 'authentication/update_data.html', {'form': form})
    else:
        return redirect('authentication/login.html')
