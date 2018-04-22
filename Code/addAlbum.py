import sqlite3
import sys

### Create the connection to the database
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

### Open the file and read it 
fh = open(sys.argv[1],"r")
artist = fh.readline()
album  = fh.readline()

sql = "SELECT id FROM playlist_manager_artist WHERE artist_name=?"
c.execute(sql, (artist.rstrip(),))
artistId = c.fetchone()
if artistId == None:
   ### Store the Artist
   c.execute("INSERT INTO playlist_manager_artist (artist_name) values (?)", (artist.rstrip(),))
   artistId = c.lastrowid
else:
   artistId = artistId[0]
print (artistId)

### Store the Album
c.execute("INSERT INTO playlist_manager_album (album_name) values (?)", (album.rstrip(),))
albumId = c.lastrowid

### Store the Artist/Album Association
c.execute("INSERT INTO playlist_manager_artist_albums (artist_id, album_id) VALUES (?, ?)", (artistId, albumId))

song = fh.readline()
while song:
    c.execute("INSERT INTO playlist_manager_song (song_name, album_name, artist_name) values (?, ?, ?)", (song.rstrip(), album.rstrip(), artist.rstrip()))
    songId = c.lastrowid
    c.execute("INSERT INTO playlist_manager_album_songs (album_id, song_id) VALUES (?, ?)", (albumId, songId))
    c.execute("INSERT INTO playlist_manager_artist_songs (artist_id, song_id) VALUES (?, ?)", (artistId, songId))
    song = fh.readline()

### Close shop
fh.close()
conn.commit();
conn.close()



