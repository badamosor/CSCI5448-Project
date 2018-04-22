from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .ItemElement import ItemElement

# Create your models here.

class Song(models.Model, ItemElement):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200, default='')
    album_name = models.CharField(max_length=200, default='')
    #artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    #album = modlels.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_name

    def accept (self, visitor):
        return visitor.visit(self)

class Album(models.Model, ItemElement):
    album_name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.album_name

    def accept (self, visitor):
        return visitor.visit(self)

class Artist(models.Model, ItemElement):
    artist_name = models.CharField(max_length=200)
    albums = models.ManyToManyField(Album)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.artist_name

    def accept (self, visitor):
        return visitor.visit(self)

class Playlist(models.Model):
    playlist_name = models.CharField(max_length = 200, help_text="Enter a playlist name")
    playlist_description = models.CharField(max_length = 1000, help_text="Enter a discription for your playlist", default = '')
    #owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null = True, related_name = 'playlist')
    owner = models.ManyToManyField(User)
    collaborative_status = models.BooleanField(default = False)
    shared_status = models.BooleanField(default = False)
    
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.playlist_name
