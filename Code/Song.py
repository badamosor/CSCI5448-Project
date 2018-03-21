import DBQuery

class Song():

   def getName(self, id):
       sql = "SELECT name FROM Song WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

if __name__ == '__main__':
    mySong = Song()
    print ("\n*** Song name ***")
    print (mySong.getName(1))
