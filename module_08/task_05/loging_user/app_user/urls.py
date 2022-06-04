from django.urls import path
from app_user.views import AuthLoginView, AuthLogoutView
from loging_user.views import MainView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('login/', AuthLoginView.as_view(), name='login'),
]
