from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Song(models.Model):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200, default='')
    album_name = models.CharField(max_length=200, default='')
    #artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    #album = modlels.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_name

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.album_name

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    albums = models.ManyToManyField(Album)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.artist_name

class Playlist(models.Model):
    playlist_name = models.CharField(max_length = 200, help_text="Enter a playlist name")
    playlist_description = models.CharField(max_length = 1000, help_text="Enter a discription for your playlist", default = '')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null = True, related_name = 'playlist')
    collaborative_status = models.BooleanField(default = False)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.playlist_name
