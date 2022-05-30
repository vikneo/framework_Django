from django.urls import path
from . import views
from advertisements.views import AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('', views.AdvertisementTitle.as_view(), name='intro'),
    path('advertisements/', AdvertisementListView.as_view(), name='advertisement'),
    path('advertisements/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement-detail'),
]