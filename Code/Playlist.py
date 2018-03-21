import DBQuery
import Song

class Playlist ():

    songs = []
    collaboration = False;

    def addSong(self, id):
        self.songs.append(id)

    def addSongs(self, ids):
        self.songs.extend(ids)

    def deleteSong(self, id):
        self.songs.remove(id)
    
    def setCollaboration (self, setCollab):
        self.collaboration = setCollab

    def getCollaboration (self):
        return self.collaboration

    def getSongs(self):
        return self.songs
    

if __name__ == '__main__':

    myPlaylist = Playlist()

### Add a song
    myPlaylist.addSong(2)

### Add a list of songs
    myPlaylist.addSongs([1, 3])
    print myPlaylist.getSongs()

### Delete a song 
    myPlaylist.deleteSong(1)
    print myPlaylist.getSongs()

### Set and get collaboration    
    myPlaylist.setCollaboration(1)
    print myPlaylist.getCollaboration()
    myPlaylist.setCollaboration(0)
    print myPlaylist.getCollaboration()

