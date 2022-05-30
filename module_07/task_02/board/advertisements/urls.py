from django.urls import path
from advertisements.views import AdvertisementsListView, IndexList, AdvertisementsDetailView

urlpatterns = [
   path("", IndexList.as_view(), name='index-list'),
   path("advertisements/", AdvertisementsListView.as_view(), name='advertisements'),
   path("advertisements/<int:pk>/", AdvertisementsDetailView.as_view(), name='advertisement-detail')
]
