from django.urls import path
from app_shop.views import items_list, upload_file,model_form_file

urlpatterns = [
    path('', items_list, name='items_list'),
    path('upload/', upload_file, name='upload'),
    path('upload_file/', model_form_file, name='upload_file'),
]
