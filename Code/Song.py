import DBQuery

class Song():

   def getName(self, id):
       sql = "SELECT name FROM Song WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

mySong = Song()
print ("\n*** Song name ***")
print (mySong.getName(1))
