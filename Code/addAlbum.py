import sqlite3
import sys

### Create the connection to the database
conn = sqlite3.connect('music.db')
c = conn.cursor()

### Open the file and read it 
fh = open(sys.argv[1],"r")
artist = fh.readline()
album  = fh.readline()

### Store the Artist
c.execute("INSERT INTO Artist (name) values (?)", (artist,))
artistId = c.lastrowid

### Store the Album
c.execute("INSERT INTO Album (name) values (?)", (album,))
albumId = c.lastrowid

song = fh.readline()
while song:
    c.execute("INSERT INTO Song (name) values (?)", (song,))
    songId = c.lastrowid
    c.execute("INSERT INTO Album2Song VALUES (?, ?)", (albumId, songId))
    c.execute("INSERT INTO Artist2Song VALUES (?, ?)", (artistId, songId))
    song = fh.readline()

### Close shop
fh.close()
conn.commit();
conn.close()
