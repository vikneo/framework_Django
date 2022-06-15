from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from app_user.forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from app_user.models import Profile


class AuthLoginView(LoginView):
    template_name: str = 'app_user/login.html'


class AuthLogoutView(LogoutView):
    # template_name = 'app_user/index.html'
    next_page = '/'


class AccountView(generic.ListView):
    model = User
    template_name = 'app_user/account.html'
    context_object_name = 'user_account'


def register_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            rew_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=rew_password)
            login(request, user)  # Логирование пользователя
            return redirect('/')  # перенаправление на главную страницу
    else:
        form = UserCreationForm()
    return render(request, 'app_user/register.html', context={'form': form})


def another_register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            birth_day = form.cleaned_data.get('birth_day')
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            discount = form.cleaned_data.get('discount')
            Profile.objects.create(
                user=user,
                birth_day=birth_day,
                city=city,
                phone=phone,
                discount=discount
            )
            username = form.cleaned_data.get('username')
            rew_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=rew_password)
            login(request, user)  # Логирование пользователя
            return redirect('/')  # перенаправление на главную страницу
    else:
        form = RegisterForm()
    return render(request, 'app_user/register.html', context={'form': form})