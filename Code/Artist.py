import DBQuery
import Song
import Album

class Artist ():

   def getName(self, id):
       sql = "SELECT name FROM Artist  WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

   def getSongs(self, id):
       sql = "SELECT songId FROM Artist2Song WHERE artistId=?"
       return (DBQuery.getList(sql, id))

   def getAlbums(self, id):
       sql = "SELECT albumId FROM Artist2Album WHERE artistId=?"
       return (DBQuery.getList(sql, id))

   def find(self, pattern):
       sql = "SELECT id FROM Artist  WHERE name LIKE {}".format("\'%"+pattern+"%\'")
       return (DBQuery.find(sql))

if __name__ == '__main__':
   myArtist = Artist ()
   mySong   = Song.Song ()
   myAlbum  = Album.Album ()

   ### Get the artist name
   print ("\n*** Artist Name ***")
   print (myArtist.getName(1))

   ### Get the songs for the artist
   print ("\n*** Song Names ***")
   songs = myArtist.getSongs(1)
   for song in songs:
      print (mySong.getName(song[0]))

   ### Get the albums for the artist
   print ("\n*** Album Names ***")
   albums = myArtist.getAlbums(1)
   for album in albums:
      print (myAlbum.getName(album[0]))

   ### Find albums with pattern
   print ("\n*** Artist Name ***")
   id = myArtist.find ('waits')
   print (myArtist.getName(id[0][0]))
