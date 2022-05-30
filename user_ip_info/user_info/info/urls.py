from django.urls import path
from .import views

urlpatterns = [
    path("user_ip", views.user_ip, name='user_list')
]