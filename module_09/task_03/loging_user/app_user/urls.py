from django.urls import path
from app_user.views import AuthLoginView, AuthLogoutView, register_view, another_register_view, AccountView
from loging_user.views import MainView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('login/', AuthLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('register_new/', another_register_view, name='register_new'),
    path('account/', AccountView.as_view(), name='account')
]
