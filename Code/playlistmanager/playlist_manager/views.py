from django.shortcuts import get_object_or_404, get_list_or_404, render
from .forms import UserForm, PlaylistForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse
from .models import Artist, Album, Song, Playlist
from django.db.models import Q

from playlist_manager import export

import logging
import itertools

class Index(View):
    def get(self,request):
        context = {}
        return render(request, 'playlist_manager/index.html', context)

class UserCreator(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'playlist_manager/create_user.html', {'form': form})
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return HttpResponseRedirect('/playlistmanager/welcome')

class ArtistList(View):
    def get(self,request):
        artist_list = Artist.objects.order_by('artist_name')[:5]
        context = {'artist_list': artist_list,}
        return render(request, 'playlist_manager/artist_list.html', context)

class ArtistDetail(View):
    def get(self,request, artist_id):
        artist = get_object_or_404(Artist, pk=artist_id)
        albums = get_list_or_404(artist.albums.order_by('album_name'))
        songs = get_list_or_404(artist.songs.order_by('song_name'))
        return render(request, 'playlist_manager/artist_detail.html', {'artist': artist, 'albums': albums, 'songs': songs})

class AlbumDetail(View):
    def get(self, request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        songs = get_list_or_404(album.songs.order_by('song_name'))
        return render(request, 'playlist_manager/album_detail.html', {'album': album, 'songs': songs})

class SongDetail(View):
    def get(self, request, song_id):
        song = get_object_or_404(Song, pk=song_id)
        return render(request, 'playlist_manager/song_detail.html', {'song': song})

class PlaylistList(View):
    def get(self, request):
        current_user = request.user
        playlist_list = Playlist.objects.filter(owner=current_user).order_by('playlist_name')
        context = {'playlist_list': playlist_list}
        return render(request, 'playlist_manager/playlist_list.html', context)

class PlaylistDetail(View):
    def get(self, request, playlist_id):
        playlist = get_object_or_404(Playlist, pk=playlist_id)
        songs = playlist.songs.order_by('song_name')
        return render(request, 'playlist_manager/playlist_detail.html', {'playlist': playlist, 'songs': songs})

class PlaylistCreator(View):
    def get(self, request):
        form = PlaylistForm()
        return render(request, 'playlist_manager/create_playlist.html', {'form': form})
    def post(self, request):
        form = PlaylistForm(request.POST)
        current_user = request.user
        if form.is_valid():
            playlist_name = form.cleaned_data.get('playlist_name')
            playlist_description = form.cleaned_data.get('playlist_description')
            collaborative_status = form.cleaned_data.get('collaborative_status')
            new_playlist = Playlist(playlist_name=playlist_name, playlist_description=playlist_description, collaborative_status = collaborative_status)
            new_playlist.save()
            new_playlist.owner.add(current_user)
            return HttpResponseRedirect('/playlistmanager/welcome')

class PlaylistEditor(View):
    def get(self, request, song_id):
        song = get_object_or_404(Song, pk=song_id)
        current_user = request.user
        playlists = Playlist.objects.filter(Q(owner=current_user) | Q(collaborative_status = True)).order_by('playlist_name')
        return render(request, 'playlist_manager/add_song_to_playlist.html', {'playlists': playlists})
    def post(self, request, song_id):
        song = get_object_or_404(Song, pk=song_id)
        logging.warning(type(song_id))
        current_user = request.user
        playlists = Playlist.objects.filter(Q(owner=current_user) | Q(collaborative_status = True)).order_by('playlist_name')
        #playlists = Playlist.objects.filter(owner=current_user).order_by('playlist_name')
        try:
            selected_playlist = playlists.get(pk=request.POST['playlist'])
        except (KeyError, Playlist.DoesNotExist):
            return render(request, 'playlist_manager/add_song_to_playlist', {'playlists': playlists,\
            'error_message': "You didn't select a playlist"})
        else:
            selected_playlist.songs.add(song)
            return render(request, 'playlist_manager/add_song_to_playlist.html', {'playlists': playlists,\
            'success_message': 'Added '+song.song_name+'to playlist '+selected_playlist.playlist_name})

class Export(View):
    def get(self, request, playlist_id):
        return render(request, 'playlist_manager/export.html', {})
    def post(self, request, playlist_id):
        current_playlist = get_object_or_404(Playlist, pk=playlist_id)
        songs = current_playlist.songs.order_by('song_name')
        song_list = list(songs)
        song_list_strings = [str(x) for x in song_list]
        exp = export.Exporter(0,song_list_strings)
        exp.execute()
        return render(request, 'playlist_manager/export.html', {})

class Welcome(View):
    def get(self, request):
        current_user = request.user
        artist_list = Artist.objects.order_by('artist_name')[:5]
        playlist_list = Playlist.objects.filter(owner=current_user).order_by('playlist_name')
        playlist_list_collaborative = Playlist.objects.filter(collaborative_status=True).order_by('playlist_name')

        context = {'artist_list': artist_list,'playlist_list': playlist_list, 'playlist_list_collaborative': playlist_list_collaborative}
        return render(request, 'playlist_manager/welcome.html', context)

class Follower(View):
    def get(self, request, playlist_id):
        current_user = request.user
        current_playlist = get_object_or_404(Playlist, pk=playlist_id)
        current_playlist.owner.add(current_user)
        current_playlist.save()
        return render(request, 'playlist_manager/follow_playlist.html', {'current_playlist': current_playlist})
