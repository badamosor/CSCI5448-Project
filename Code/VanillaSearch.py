import DBQuery

class Song():

   def getName(self, id):
       sql = "SELECT name FROM Song WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

   def find(self, pattern):
       sql = "SELECT id FROM Song  WHERE name LIKE {}".format("\'%"+pattern+"%\'")
       return (DBQuery.find(sql))

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

class Album ():

   def getName(self, id):
       sql = "SELECT name FROM Album  WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

   def getSongs(self, id):
       sql = "SELECT songId FROM Album2Song  WHERE albumId=?"
       return (DBQuery.getList(sql, id))

   def find(self, pattern):
       sql = "SELECT id FROM Album  WHERE name LIKE {}".format("\'%"+pattern+"%\'")
       return (DBQuery.find(sql))

class SearchVanilla():

   def searchDatabase (self, items, term):
      for item in items:
          if isinstance(item, Song):
              print ("These are the Song matches: ")
          elif isinstance(item, Artist):
              print ("These are the Artist matches: ")
          elif isinstance(item, Album):
              print ("These are the Album matches: ")
          for match in item.find(term):
              print ("    " + item.getName(match[0]))

if __name__ == '__main__':
    print ("\nSearch Term: the")
    items = [ Song(), Album(), Artist() ]

    sv = SearchVanilla()
    
    total = sv.searchDatabase(items, "the")
    print ("\n\nSearch Term: Blue")
    total = sv.searchDatabase(items, "Blue")
