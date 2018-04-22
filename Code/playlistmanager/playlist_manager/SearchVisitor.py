from .MusicVisitorImplementation import MusicVisitorImplementation

class SearchVisitor():

    def searchDatabase (self, items, term):
        visitor = MusicVisitorImplementation(term)
        for item in items:
            results = item.accept(visitor)
        return results
