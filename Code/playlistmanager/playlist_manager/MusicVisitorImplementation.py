from .MusicVisitor import MusicVisitor
from .models import Artist, Album, Song

class MusicVisitorImplementation(MusicVisitor):

    def __init__(self, pattern):
        self.pattern = pattern
        self.results ={}

    def visit(self, item):
        if isinstance(item, Song):
            self.results['song']  = Song.objects.filter(song_name__contains=self.pattern)
        elif isinstance(item, Artist):
            self.results['artist']  = Artist.objects.filter(artist_name__contains=self.pattern)
        elif isinstance(item, Album):
            self.results['album']  = Album.objects.filter(album_name__contains=self.pattern)
        return self.results

