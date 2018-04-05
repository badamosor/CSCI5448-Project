from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('<int:album_id>/album', views.album_detail, name='album_detail'),
    path('<int:song_id>/song', views.song_detail, name='song_detail'),
]
