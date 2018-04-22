import DBQuery

class ItemElement():
    def accept(self):
        pass

class MusicVisitor():
    def visit(self, item):
        pass

class Song(ItemElement):

   def getName(self, id):
       sql = "SELECT name FROM Song WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

   def find(self, pattern):
       sql = "SELECT id FROM Song  WHERE name LIKE {}".format("\'%"+pattern+"%\'")
       return (DBQuery.find(sql))

   def accept(self, visitor):
       return visitor.visit(self)

class Artist (ItemElement):

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

   def accept(self, visitor):
       return visitor.visit(self)

class Album (ItemElement):

   def getName(self, id):
       sql = "SELECT name FROM Album  WHERE id=?"
       return (DBQuery.getOne(sql, id)[0])

   def getSongs(self, id):
       sql = "SELECT songId FROM Album2Song  WHERE albumId=?"
       return (DBQuery.getList(sql, id))

   def find(self, pattern):
       sql = "SELECT id FROM Album  WHERE name LIKE {}".format("\'%"+pattern+"%\'")
       return (DBQuery.find(sql))

   def accept(self, visitor):
       return visitor.visit(self)

class MusicVisitorImplementation(MusicVisitor):

    def __init__(self, pattern):
        self.pattern = pattern
        self.results ={}

    def visit(self, item):
        if isinstance(item, Song):
            print ("These are the Song matches: ")
            self.results['song']  = item.find(self.pattern)
        elif isinstance(item, Artist):
            print ("These are the Artist matches: ")
            self.results['artist']  = item.find(self.pattern)
        elif isinstance(item, Album):
            print ("These are the Album matches: ")
            self.results['album']  = item.find(self.pattern)

        for match in item.find(self.pattern):
            print ("    " + item.getName(match[0]))

        return self.results


class SearchVisitor():

    
    def searchDatabase (self, items, term):
        visitor = MusicVisitorImplementation(term)
        for item in items:
            results = item.accept(visitor)
        return results

if __name__ == '__main__':
    print ("\nSearch Term: the")
    items = [ Song(), Album(), Artist() ]

    sv = SearchVisitor()

    total = sv.searchDatabase(items, "the")
    print ("\n\nSearch Term: Blue")
    total = sv.searchDatabase(items, "Blue")

    print (total)

   
