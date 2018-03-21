import DBQuery
import Playlist
import sys

class User ():
 
    password = ""
    email = ""
    collaborating = []
    playlists = []

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email
    
    def createPlaylist(self, name):
        myPlaylist = Playlist.Playlist(name)
        self.playlists.append (myPlaylist.getId())
        return myPlaylist
    
    def getPlaylists(self):
        return self.playlists

    def addCollaboration(self, playlist):
        playlist.setCollaboration(True);
    
if __name__ == '__main__':

    myUser = User()

### Set and get Password 
    myUser.setPassword("123")
    print ("password: " +  myUser.getPassword())

### Set and get Email 
    myUser.setEmail("abc@example.com")
    print ("Email: " +  myUser.getEmail())

### Create a playlist
    ABC = myUser.createPlaylist('ABC')
    DEF = myUser.createPlaylist('DEF')
    OPQ = myUser.createPlaylist('OPQ')
    print ("Created playlist id: ", ABC.getId())
    print ("Created playlist id: ", DEF.getId())
    print ("Created playlist id: ", OPQ.getId())

### Get playlists
    print ("Playlists: ", myUser.getPlaylists())

### Add songs to a playlist
    ABC.addSong(2)
    ABC.addSongs([2, 3, 4, 5])

    DEF.addSong(11)
    DEF.addSongs([2, 3, 16, 1])

### Delete song

    ABC.deleteSong(2)

### Add collaboration
    print ("Collaboration before:", ABC.getCollaboration())
    myUser.addCollaboration(ABC);
    print ("Add collaboration:", ABC.getCollaboration())


### Get songs

    print DEF.getSongs()
