import datetime

class SpotifySongSearcher():
    def getSongIDs(self, songList):
        songIDs = []
        for song in songList:
            songIDs.append(len(song)*ord(song[0])) #some fake way to get IDs
        return songIDs


class SpotifyPlaylistBuilder():
    def playlistBuilder(self, songIDs):
        playlist = []
        for id in songIDs:
            playlist.append((id,"Spotify"))
        return playlist

class SpotifyPlaylistWriter():
    def playlistWriter(self, playlist):
        f = open("export.txt", "a")
        for song in playlist:
            f.write(str(song[0]) + " " + song[1] + " "+ str(datetime.datetime.now())+"\n")

class SpotifyExportFacade():
    songList = []
    spotifySongSearcher = None
    spotifyPlaylistBuilder = None
    spotifyPlaylistWriter = None
    def __init__(self, songList):
        self.songList = songList
        self.spotifySongSearcher = SpotifySongSearcher()
        self.spotifyPlaylistBuilder = SpotifyPlaylistBuilder()
        self.spotifyPlaylistWriter = SpotifyPlaylistWriter()

    def runExport(self):
        songIDs = self.spotifySongSearcher.getSongIDs(self.songList)
        builtPlaylist = self.spotifyPlaylistBuilder.playlistBuilder(songIDs)
        self.spotifyPlaylistWriter.playlistWriter(builtPlaylist)

class TidalSongSearcher():
    def getSongIDs(self, songList):
        songIDs = []
        for song in songList:
            songIDs.append(len(song)*ord(song[0])) #some fake way to get IDs
        return songIDs


class TidalPlaylistBuilder():
    def playlistBuilder(self, songIDs):
        playlist = []
        for id in songIDs:
            playlist.append((id,"Tidal"))
        return playlist

class TidalPlaylistWriter():
    def playlistWriter(self, playlist):
        f = open("export.txt", "a")
        for song in playlist:
            f.write(str(song[0]) + " " + song[1] + " "+ str(datetime.datetime.now())+"\n")

class TidalExportFacade():
    songList = []
    TidalSongSearcher = None
    TidalPlaylistBuilder = None
    TidalPlaylistWriter = None
    def __init__(self, songList):
        self.songList = songList
        self.TidalSongSearcher = TidalSongSearcher()
        self.TidalPlaylistBuilder = TidalPlaylistBuilder()
        self.TidalPlaylistWriter = TidalPlaylistWriter()

    def runExport(self):
        songIDs = self.TidalSongSearcher.getSongIDs(songList)
        builtPlaylist = self.TidalPlaylistBuilder.playlistBuilder(songIDs)
        self.TidalPlaylistWriter.playlistWriter(builtPlaylist)

class GooglePlaySongSearcher():
    def getSongIDs(self, songList):
        songIDs = []
        for song in songList:
            songIDs.append(len(song)*ord(song[0])) #some fake way to get IDs
        return songIDs


class GooglePlayPlaylistBuilder():
    def playlistBuilder(self, songIDs):
        playlist = []
        for id in songIDs:
            playlist.append((id,"Google Play"))
        return playlist

class GooglePlayPlaylistWriter():
    def playlistWriter(self, playlist):
        f = open("export.txt", "a")
        for song in playlist:
            f.write(str(song[0]) + " " + song[1] + " "+ str(datetime.datetime.now())+"\n")

class GooglePlayExportFacade():
    songList = []
    GooglePlaySongSearcher = None
    GooglePlayPlaylistBuilder = None
    GooglePlayPlaylistWriter = None
    def __init__(self, songList):
        self.songList = songList
        self.GooglePlaySongSearcher = GooglePlaySongSearcher()
        self.GooglePlayPlaylistBuilder = GooglePlayPlaylistBuilder()
        self.GooglePlayPlaylistWriter = GooglePlayPlaylistWriter()

    def runExport(self):
        songIDs = self.GooglePlaySongSearcher.getSongIDs(songList)
        builtPlaylist = self.GooglePlayPlaylistBuilder.playlistBuilder(songIDs)
        self.GooglePlayPlaylistWriter.playlistWriter(builtPlaylist)

class Exporter():
    serviceId = -1
    exportStrategy = None
    songList = []
    def __init__(self,serviceId,songList):
        self.serviceId = serviceId
        self.songList = songList
        if self.serviceId == 0:
            self.exportStrategy = ExportSpotify(songList)
        elif self.serviceId == 1:
            self.exportStrategy = ExportTidal(songList)
        elif self.serviceId == 2:
            self.exportStrategy = ExportGooglePlay(songList)

    def execute(self):
        self.exportStrategy.export()

    def __str__(self):
        print(self.serviceId)

class AbstractExporterStrategy():
    songList = []
    def __init__(self, songList):
        raise NotImplementedError("This is abstract")
    def export(self):
        raise NotImplementedError("This is abstract")

class ExportSpotify(AbstractExporterStrategy):
    songList = []
    spotifyExport = None
    def __init__(self, songList):
        self.songList = songList
        self.spotifyExport = SpotifyExportFacade(songList)
    def export(self):
        self.spotifyExport.runExport()

class ExportTidal(AbstractExporterStrategy):
    songList = []
    tidalExport = None
    def __init__(self, songList):
        self.songList = songList
        self.tidalExport = TidalExportFacade(songList)
    def export(self):
        self.tidalExport.runExport()

class ExportGooglePlay(AbstractExporterStrategy):
    songList = []
    googlePlayExport = None
    def __init__(self, songList):
        self.songList = songList
        self.googlePlayExport = GooglePlayExportFacade(songList)
    def export(self):
        self.googlePlayExport.runExport()
