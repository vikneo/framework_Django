from django.urls import path
from app_user.views import AuthLoginView
from loging_user.viesw import MainView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', AuthLoginView.as_view(), name='login'),
]
