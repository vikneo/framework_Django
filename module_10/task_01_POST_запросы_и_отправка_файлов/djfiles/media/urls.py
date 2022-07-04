from django.urls import path
from media.views import upload_file, read_file


urlpatterns = [
    path('file/', upload_file, name='upload-file'),
    path('read/', read_file, name='read-file'),
]
