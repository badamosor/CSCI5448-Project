import sqlite3

conn = sqlite3.connect('music.db')
c = conn.cursor()

c.execute('''CREATE TABLE Song (id integer primary key autoincrement, name text)''')
c.execute('''CREATE TABLE Album (id integer primary key autoincrement, name text)''')
c.execute('''CREATE TABLE Artist (id integer primary key autoincrement, name text)''')
c.execute('''CREATE TABLE Album2Song (albumId INT, songId INT)''')
c.execute('''CREATE TABLE Artist2Song (artistId INT, songId INT)''')
c.execute('''CREATE TABLE Artist2Album (artistId INT, AlbumId INT)''')

conn.close()
