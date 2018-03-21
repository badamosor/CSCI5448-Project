import DBQuery
import Playlist
import sqlite3
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
        conn = sqlite3.connect('music.db')
        c = conn.cursor()

        c.execute("INSERT INTO Playlist (name) values (?)", (name,))
        playlistId = c.lastrowid
        conn.commit()
        conn.close()
        self.playlists.append(playlistId)
        return playlistId
        
    
if __name__ == '__main__':

    myUser = User()

### Set and get Password 
    myUser.setPassword("123")
    print ("password: " +  myUser.getPassword())

### Set and get Email 
    myUser.setEmail("abc@example.com")
    print ("Email: " +  myUser.getEmail())

### Create a playlist
    print ("Created playlist id: ", myUser.createPlaylist('TestPlaylist'))
