from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from advertisements.forms import AdvertisementForms
from advertisements.models import Advertisement


class AdvertisementFormView(View):

    def get(self, request):
        advertisements = AdvertisementForms()
        return render(request, 'advertisements/advertisement_info.html', context={"advertisements": advertisements})

    def post(self, request):
        advertisements = AdvertisementForms(request.POST)

        if advertisements.is_valid():
            print(request.POST)
            # совершаем какую либо логику
            # в данном случае сохраняем в базу данных
            Advertisement.objects.create(**advertisements.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, "advertisements/advertisement_detail.html", context={'advertisements': advertisements})

# пока не верно с выводом результата, НО ЗАПИСЬ ЕСТЬ В БД
