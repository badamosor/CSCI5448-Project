from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('artist_list', views.artist_list, name='artist_list'),
    path('<int:song_id>/add_song_to_playlist', views.add_song_to_playlist, name='add_song_to_playlist'),
    path('playlist_list', views.playlist_list, name='playlist_list'),
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('<int:album_id>/album', views.album_detail, name='album_detail'),
    path('<int:song_id>/song', views.song_detail, name='song_detail'),
    path('<int:playlist_id>/playlist', views.playlist_detail, name='playlist_detail'),
]
