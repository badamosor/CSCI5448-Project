from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from .views import Index, ArtistList, ArtistDetail, AlbumDetail,SongDetail,\
Welcome, PlaylistDetail, PlaylistList, PlaylistCreator, UserCreator, PlaylistEditor, \
Export, Follower, PlaylistSharer
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('welcome', login_required(Welcome.as_view()), name='welcome'),
    path('create_user/', UserCreator.as_view(), name='create_user'),
    path('create_playlist/', login_required(PlaylistCreator.as_view()), name='create_playlist'),
    path('artist_list', login_required(ArtistList.as_view())),
    path('<int:song_id>/add_song_to_playlist', login_required(PlaylistEditor.as_view()), name='add_song_to_playlist'),
    path('playlist_list', login_required(PlaylistList.as_view()), name='playlist_list'),
    path('<int:artist_id>/', login_required(ArtistDetail.as_view()), name='artist_detail'),
    path('<int:album_id>/album', login_required(AlbumDetail.as_view()), name='album_detail'),
    path('<int:song_id>/song', login_required(SongDetail.as_view()), name='song_detail'),
    path('<int:playlist_id>/playlist', login_required(PlaylistDetail.as_view()), name='playlist_detail'),
    path('<int:playlist_id>/export/', login_required(Export.as_view()), name='export'),
    path('<int:playlist_id>/follow_playlist/', login_required(Follower.as_view()), name='follow'),
    path('<int:playlist_id>/share_playlist/', login_required(PlaylistSharer.as_view()), name='share'),
]
