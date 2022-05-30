from django.urls import path
from app_user.views import login_user


urlpatterns = [
    path('login/', login_user, name='login'),
]
