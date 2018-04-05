from django.shortcuts import get_object_or_404, get_list_or_404, render
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .models import Artist, Album, Song

# Create your views here.
def index(request):
    context = {}
    return render(request, 'playlist_manager/index.html', context)

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return HttpResponseRedirect('/playlistmanager/artist_list')
    else:
        form = UserForm()

    return render(request, 'playlist_manager/create_user.html', {'form': form})

def login(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request,user)
    #     return HttpResponseRedirect('/playlistmanager/artist_list')
    #
    # return render(request, 'playlist_manager/login.html', {})
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.username
            password =  form.password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, new_user)
                return HttpResponseRedirect('/playlistmanager/artist_list')
            else:
                return HttpResponseRedirect('/playlistmanager/')

    else:
        form = UserForm()

    return render(request, 'playlist_manager/login.html', {'form': form})

def artist_list(request):
    artist_list = Artist.objects.order_by('artist_name')[:5]
    context = {'artist_list': artist_list,}
    return render(request, 'playlist_manager/artist_list.html', context)

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
