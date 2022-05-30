from django.urls import path

from app_news.views import NewsFormView, NewsCreateFormView

urlpatterns = [
    path("", NewsFormView.as_view(), name='news-list'),
    path('news_create/', NewsCreateFormView.as_view(), name='news-created')
]