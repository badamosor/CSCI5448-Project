import DBQuery
import Song

class Playlist ():

    songs = []

    def addSong(self, id):
        self.songs.append(id)

    def addSongs(self, ids):
        self.songs.extend(ids)

    def deleteSong(self, id):
        self.songs.remove(id)

    def getSongs(self):
        return self.songs
    

if __name__ == '__main__':
    myPlaylist = Playlist()
    myPlaylist.addSong(2)
    myPlaylist.addSongs([1, 3])
    print myPlaylist.getSongs()
    myPlaylist.deleteSong(1)
    print myPlaylist.getSongs()

