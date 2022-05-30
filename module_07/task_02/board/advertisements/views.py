from django.shortcuts import render
from django.views import View, generic
from advertisements.models import Advertisement


class IndexList(View):

    def get(self, request):
        titles = 'Добро пожаловать!'
        return render(request, 'advertisements/advertisement_title.html', {'titles': titles})


class AdvertisementsListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:10]


class AdvertisementsDetailView(generic.DetailView):
    model = Advertisement

    def get_object(self, queryset=None):
        views = super(AdvertisementsDetailView, self).get_object()
        views.view_count += 1
        views.save()
        return views
