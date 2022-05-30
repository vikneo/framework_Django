from django.urls import path
from . import views


urlpatterns = [
    path("", views.advertisement_title, name='advertisement_title')
]