from django.shortcuts import render
from django.views import generic, View
from advertisements.models import Advertisement


class AdvertisementTitle(View):

    def get(self, request):
        intro = 'Добро пожаловать на сайт бесплатных объявлений'
        return render(request, 'advertisements/advertisement_title.html', {'intro': intro})


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

    def get_object(self, queryset=None):
        view = super().get_object()
        view.view_count += 1
        view.save()
        return view


