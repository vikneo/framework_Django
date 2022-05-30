from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from app_user.forms import AuthForm
from datetime import datetime


def login_user(request):
    date = datetime.now()

    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_superuser:   # проверка на администратора
                    if 20 <= date.hour <= 8:   # проверка на время доступа
                        if user.is_active:   # проверка на активность пользователя
                            login(request, user)
                            return HttpResponse('Вы успешно авторизовались')
                        else:
                            auth_form.add_error('__all__', 'Данный пользователь не активен')
                            return HttpResponse('Данный пользователь не активен')
                    else:
                        auth_form.add_error('__all__', 'С 20:00 до 8:00 вход запрещен')
                        return HttpResponse('С 20:00 до 8:00 вход запрещен')
                else:
                    auth_form.add_error('__all__', 'Запрещено администраторам')
                    return HttpResponse('Запрещено администраторам')
            else:
                auth_form.add_error('__all__', 'Данного пользователя не существует')
                return HttpResponse('Данного пользователя не существует')
    auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'app_user/login.html', context=context)
