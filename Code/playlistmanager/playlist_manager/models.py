from django.db import models

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
