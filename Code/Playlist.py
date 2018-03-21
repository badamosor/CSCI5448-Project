import DBQuery
import Song

class Playlist ():
 
    discription = ""
    songs = []
    collaboration = False

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
    
    def setDiscription (self, text):
        self.description = text

    def getDiscription (self):
        return self.description
    
if __name__ == '__main__':

    myPlaylist = Playlist()

### Set discription 
    myPlaylist.setDiscription("This is a test playlist.")

### Get discription
    print myPlaylist.getDiscription()

### Add a song
    myPlaylist.addSong(2)

### Add a list of songs
    myPlaylist.addSongs([1, 3])
    print myPlaylist.getSongs()

### Delete a song 
    myPlaylist.deleteSong(1)
    print myPlaylist.getSongs()
    
### Print song names 
    mySongs = Song.Song()
    mySongIds = myPlaylist.getSongs()
    for id in mySongIds:
        print mySongs.getName(id)

        

### Set and get collaboration    
    myPlaylist.setCollaboration(1)
    print myPlaylist.getCollaboration()
    myPlaylist.setCollaboration(0)
    print myPlaylist.getCollaboration()

