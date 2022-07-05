from django.urls import path
from app_shop.views import items_list, upload_file

urlpatterns = [
    path('', items_list, name='items_list'),
    path('upload/', upload_file, name='upload'),
]
