import DBQuery

class Song():

   def getName(self, id):
       sql = "SELECT name FROM Song WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

   def find(self, pattern):
       sql = "SELECT id FROM Song  WHERE name LIKE {}".format("\'%"+pattern+"%\'")
       return (DBQuery.find(sql))

if __name__ == '__main__':
    mySong = Song()
    print ("\n*** Song name ***")
    print (mySong.getName(1))

    ### Find songs with pattern
    print ("\n*** Song Name ***")
    ids = mySong.find ('the')
    for id in ids:
       print (mySong.getName(id[0]))
