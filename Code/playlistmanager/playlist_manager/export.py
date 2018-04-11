import datetime

class SpotifySongSearch():
    def getSongIDs(self, songList):
        songIDs = []
        for song in songList:
            songIDs.append(len(song)*ord(song[0])) #some fake way to get IDs
        return songIDs


class SpotifyBuildPlaylist():
    def buildPlaylist(self, songIDs):
        playlist = []
        for id in songIDs:
            playlist.append((id,"Spotify"))
        return playlist

class SpotifyWritePlaylist():
    def writePlaylist(self, playlist):
        f = open("export.txt", "a")
        for song in playlist:
            f.write(str(song[0]) + " " + song[1] + " "+ str(datetime.datetime.now())+"\n")

class SpotifyExportFacade():
    songList = []
    spotifySongSearch = None
    spotifyBuildPlaylist = None
    spotifyWritePlaylist = None
    def __init__(self, songList):
        self.songList = songList
        self.spotifySongSearch = SpotifySongSearch()
        self.spotifyBuildPlaylist = SpotifyBuildPlaylist()
        self.spotifyWritePlaylist = SpotifyWritePlaylist()

    def runExport(self):
        songIDs = self.spotifySongSearch.getSongIDs(self.songList)
        builtPlaylist = self.spotifyBuildPlaylist.buildPlaylist(songIDs)
        self.spotifyWritePlaylist.writePlaylist(builtPlaylist)

class TidalSongSearch():
    def getSongIDs(self, songList):
        songIDs = []
        for song in songList:
            songIDs.append(len(song)*ord(song[0])) #some fake way to get IDs
        return songIDs


class TidalBuildPlaylist():
    def buildPlaylist(self, songIDs):
        playlist = []
        for id in songIDs:
            playlist.append((id,"Tidal"))
        return playlist

class TidalWritePlaylist():
    def writePlaylist(self, playlist):
        f = open("export.txt", "a")
        for song in playlist:
            f.write(str(song[0]) + " " + song[1] + " "+ str(datetime.datetime.now())+"\n")

class TidalExportFacade():
    songList = []
    TidalSongSearch = None
    TidalBuildPlaylist = None
    TidalWritePlaylist = None
    def __init__(self, songList):
        self.songList = songList
        self.TidalSongSearch = TidalSongSearch()
        self.TidalBuildPlaylist = TidalBuildPlaylist()
        self.TidalWritePlaylist = TidalWritePlaylist()

    def runExport(self):
        songIDs = self.TidalSongSearch.getSongIDs(songList)
        builtPlaylist = self.TidalBuildPlaylist.buildPlaylist(songIDs)
        self.TidalWritePlaylist.writePlaylist(builtPlaylist)

class GooglePlaySongSearch():
    def getSongIDs(self, songList):
        songIDs = []
        for song in songList:
            songIDs.append(len(song)*ord(song[0])) #some fake way to get IDs
        return songIDs


class GooglePlayBuildPlaylist():
    def buildPlaylist(self, songIDs):
        playlist = []
        for id in songIDs:
            playlist.append((id,"Google Play"))
        return playlist

class GooglePlayWritePlaylist():
    def writePlaylist(self, playlist):
        f = open("export.txt", "a")
        for song in playlist:
            f.write(str(song[0]) + " " + song[1] + " "+ str(datetime.datetime.now())+"\n")

class GooglePlayExportFacade():
    songList = []
    GooglePlaySongSearch = None
    GooglePlayBuildPlaylist = None
    GooglePlayWritePlaylist = None
    def __init__(self, songList):
        self.songList = songList
        self.GooglePlaySongSearch = GooglePlaySongSearch()
        self.GooglePlayBuildPlaylist = GooglePlayBuildPlaylist()
        self.GooglePlayWritePlaylist = GooglePlayWritePlaylist()

    def runExport(self):
        songIDs = self.GooglePlaySongSearch.getSongIDs(songList)
        builtPlaylist = self.GooglePlayBuildPlaylist.buildPlaylist(songIDs)
        self.GooglePlayWritePlaylist.writePlaylist(builtPlaylist)

class Exporter():
    serviceId = -1
    export_strategy = None
    songList = []
    def __init__(self,serviceId,songList):
        self.serviceId = serviceId
        self.songList = songList
        if self.serviceId == 0:
            self.export_strategy = ExportSpotify(songList)
        elif self.serviceId == 1:
            self.export_strategy = ExportTidal(songList)
        elif self.serviceId == 2:
            self.export_strategy = ExportGooglePlay(songList)

    def execute(self):
        self.export_strategy.export()

    def __str__(self):
        print(self.serviceId)

class ExportInterface():
    songList = []
    def __init__(self, songList):
        raise NotImplementedError("This is abstract")
    def export(self):
        raise NotImplementedError("This is abstract")

class ExportSpotify(ExportInterface):
    songList = []
    spotifyExport = None
    def __init__(self, songList):
        self.songList = songList
        self.spotifyExport = SpotifyExportFacade(songList)
    def export(self):
        self.spotifyExport.runExport()

class ExportTidal(ExportInterface):
    songList = []
    tidalExport = None
    def __init__(self, songList):
        self.songList = songList
        self.tidalExport = TidalExportFacade(songList)
    def export(self):
        self.tidalExport.runExport()

class ExportGooglePlay(ExportInterface):
    songList = []
    googlePlayExport = None
    def __init__(self, songList):
        self.songList = songList
        self.googlePlayExport = GooglePlayExportFacade(songList)
    def export(self):
        self.googlePlayExport.runExport()
