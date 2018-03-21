from DBConnection import connection

c = connection.getCursor()
c.execute("INSERT INTO Playlist (name) VALUES (?)", ('Lullabies', ))
connection.closeCursor(c)

