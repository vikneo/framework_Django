from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, request):
        return render(request, 'app_user/index.html')

    def post(self, request):
        if request.POST['username'] == 'admin':
            # return HttpResponse('Добро пожаловать Админ!')
            return render(request, 'app_user/admin.html')
        else:
            return render(request, 'app_user/index.html')
