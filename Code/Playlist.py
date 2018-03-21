import DBQuery
import Song

class Playlist ():
    songs = []

    def addSong(self, id):
        self.songs.append(id)

if __name__ == '__main__':
    myPlaylist = Playlist()
    myPlaylist.addSong(2)

