from django.shortcuts import render
from advertisements.models import Advertisement


def advertisement_title(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement/advertisement_list.html',
                  {'advertisements': advertisements}
                  )
