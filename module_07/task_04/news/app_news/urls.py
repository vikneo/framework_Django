from django.urls import path

from app_news.views import NewsListView, CommentDetailView, RegeditNewsView, CreateNewsView

urlpatterns = [
    path("", NewsListView.as_view(), name='news-list'),
    path("create_news/", CreateNewsView.as_view(), name='create-news'),
    path("detail/<int:pk>/", CommentDetailView.as_view(), name='news-detail'),
    path("detail/<int:pk>/edit/", RegeditNewsView.as_view(), name='news-regedit')
]
