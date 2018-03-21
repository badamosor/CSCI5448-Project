from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Artist, Album, Song

# Create your views here.
def index(request):
    artist_list = Artist.objects.order_by('artist_name')[:5]
    context = {'artist_list': artist_list,}
    return render(request, 'playlist_manager/index.html', context)

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    albums = get_list_or_404(artist.albums.order_by('album_name'))
    songs = get_list_or_404(artist.songs.order_by('song_name'))
    return render(request, 'playlist_manager/artist_detail.html', {'artist': artist, 'albums': albums, 'songs': songs})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    songs = get_list_or_404(album.songs.order_by('song_name'))
    return render(request, 'playlist_manager/album_detail.html', {'album': album, 'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'playlist_manager/song_detail.html', {'song': song})
