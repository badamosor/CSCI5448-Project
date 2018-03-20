import sqlite3
import sys

### Create the connection to the database
conn = sqlite3.connect('music.db')
c = conn.cursor()

### Open the file and read it 
fh = open(sys.argv[1],"r")
artist = fh.readline()
album  = fh.readline()

sql = "SELECT id FROM Artist WHERE name=?"
c.execute(sql, (artist.rstrip(),))
artistId = c.fetchone()
if artistId == None:
   ### Store the Artist
   c.execute("INSERT INTO Artist (name) values (?)", (artist.rstrip(),))
   artistId = c.lastrowid
else:
   artistId = artistId[0]
print (artistId)

### Store the Album
c.execute("INSERT INTO Album (name) values (?)", (album.rstrip(),))
albumId = c.lastrowid

### Store the Artist/Album Association
c.execute("INSERT INTO Artist2Album VALUES (?, ?)", (artistId, albumId))

song = fh.readline()
while song:
    c.execute("INSERT INTO Song (name) values (?)", (song.rstrip(),))
    songId = c.lastrowid
    c.execute("INSERT INTO Album2Song VALUES (?, ?)", (albumId, songId))
    c.execute("INSERT INTO Artist2Song VALUES (?, ?)", (artistId, songId))
    song = fh.readline()

### Close shop
fh.close()
conn.commit();
conn.close()



