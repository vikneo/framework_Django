from django.shortcuts import render
from django.views import generic

from advertisements.models import Advertisement


def advertisement_title(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement/advertisement_title.html',
                  {'advertisements': advertisements}
                  )



