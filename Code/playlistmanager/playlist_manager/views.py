from django.shortcuts import get_object_or_404, get_list_or_404, render
from .forms import UserForm, PlaylistForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Artist, Album, Song, Playlist

import logging
logger = logging.getLogger(__name__)

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
            return HttpResponseRedirect('/playlistmanager/playlist_list')
    else:
        form = UserForm()

    return render(request, 'playlist_manager/create_user.html', {'form': form})

@login_required(login_url='/accounts/login/')
def artist_list(request):
    artist_list = Artist.objects.order_by('artist_name')[:5]
    context = {'artist_list': artist_list,}
    return render(request, 'playlist_manager/artist_list.html', context)
@login_required(login_url='/accounts/login/')

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    albums = get_list_or_404(artist.albums.order_by('album_name'))
    songs = get_list_or_404(artist.songs.order_by('song_name'))
    return render(request, 'playlist_manager/artist_detail.html', {'artist': artist, 'albums': albums, 'songs': songs})
@login_required(login_url='/accounts/login/')

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    songs = get_list_or_404(album.songs.order_by('song_name'))
    return render(request, 'playlist_manager/album_detail.html', {'album': album, 'songs': songs})

@login_required(login_url='/accounts/login/')
def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'playlist_manager/song_detail.html', {'song': song})


@login_required(login_url='/accounts/login/')
def playlist_list(request):
    current_user = request.user
    playlist_list = Playlist.objects.filter(owner=current_user).order_by('playlist_name')
    context = {'playlist_list': playlist_list}
    return render(request, 'playlist_manager/playlist_list.html', context)

@login_required(login_url='/accounts/login/')
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    songs = playlist.songs.order_by('song_name')
    logging.warning(type(songs))
    return render(request, 'playlist_manager/playlist_detail.html', {'playlist': playlist, 'songs': songs})

@login_required(login_url='/accounts/login/')
def create_playlist(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        current_user = request.user
        if form.is_valid():
            playlist_name = form.cleaned_data.get('playlist_name')
            playlist_description = form.cleaned_data.get('playlist_description')
            collaborative_status = form.cleaned_data.get('collaborative_status')
            new_playlist = Playlist(playlist_name=playlist_name, playlist_description=playlist_description, owner=current_user, collaborative_status = collaborative_status)
            new_playlist.save()
            return HttpResponseRedirect('/playlistmanager/playlist_list')
    else:
        form = PlaylistForm()

    return render(request, 'playlist_manager/create_playlist.html', {'form': form})

@login_required(login_url='/accounts/login/')
def add_song_to_playlist(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    current_user = request.user
    playlists = Playlist.objects.filter(owner=current_user).order_by('playlist_name')
    logging.warning(type(playlists))
    if request.method == "POST":
        try:
            selected_playlist = playlists.get(pk=request.POST['playlist'])
        except (KeyError, Playlist.DoesNotExist):
            return render(request, 'playlist_manager/'+song_id +'/add_song_to_playlist', {'playlists': playlists,\
            'error_message': "You didn't select a playlist"})
        else:
            selected_playlist.songs.add(song)

    return render(request, 'playlist_manager/add_song_to_playlist.html', {'playlists': playlists})

@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    artist_list = Artist.objects.order_by('artist_name')[:5]
    playlist_list = Playlist.objects.filter(owner=current_user).order_by('playlist_name')
    context = {'artist_list': artist_list,'playlist_list': playlist_list,}
    return render(request, 'playlist_manager/welcome.html', context)
