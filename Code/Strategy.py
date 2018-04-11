import Visitor as visitor
import VanillaSearch as vanilla

class StringFinder:
    """ Interface """

    def find(self, pattern):
        pass

class StringFinderVisitor(StringFinder):

    items = [visitor.Song(), visitor.Album(), visitor.Artist()] 

    def find(self, pattern):
        sv = visitor.SearchVisitor()
        sv.searchDatabase(self.items, pattern)

class StringFinderVanilla(StringFinder):

    items = [vanilla.Song(), vanilla.Album(), vanilla.Artist()] 

    def find(self, pattern):
        sv = vanilla.SearchVanilla()
        sv.searchDatabase(self.items, pattern)
    
if __name__ == "__main__" :

    finderVanilla = StringFinderVanilla()
    finderVisitor = StringFinderVisitor()

    finderVisitor.find('the')
    print ("\n")
    finderVanilla.find('Blue')
    print ("\n")
    finderVanilla.find('the')
    print ("\n")
