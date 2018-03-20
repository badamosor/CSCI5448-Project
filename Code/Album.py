import DBQuery
import Song

class Album ():

   def getName(self, id):
       sql = "SELECT name FROM Album  WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

   def getSongs(self, id):
       sql = "SELECT songId FROM Album2Song  WHERE albumId=?"
       return (DBQuery.getList(sql, id))

myAlbum  = Album ()
mySong   = Song.Song ()

### Get the album name
print ("\n*** Album Name ***")
print (myAlbum.getName(2))

### Get the songs for the album
print ("\n*** Song Names ***")
songs = myAlbum.getSongs(2)
for song in songs:
   print (mySong.getName(song[0]))
