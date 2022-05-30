from django.urls import path
from .import views


urlpatterns = [
  path("", views.advertisement_title, name='advertisement_list'),
  path("detail_python_basic/", views.advertisement_detail_python_basic, name='advertisement_list'),
  path("detail_sql/", views.advertisement_detail_sql, name='advertisement_list'),
  path("detail_django/", views.advertisement_detail_django, name='advertisement_list'),
  path("detail_python_pro/", views.advertisement_detail_python_pro, name='advertisement_list'),
  path("detail_web/", views.advertisement_detail_web, name='advertisement_list'),
  # path("", views.get_time, name='advertisement_list')
]
