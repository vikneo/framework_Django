from django.urls import path
from .import views


urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path("contacts/", views.contacts_list, name='contacts'),
    path("about/", views.about, name='about_list'),
    path("about/categories/", views.about_list, name='about_list'),
    path("private/", views.board_list, name='private'),
    path("region/", views.region, name='region'),
    path('region/add/', views.Regions.as_view()),
    path('region/city/', views.Regions.as_view()),
    path("region/city/", views.region, name='region'),
]
