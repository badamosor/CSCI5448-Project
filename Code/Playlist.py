import DBQuery
import sys
import sqlite3

class Playlist():

    name = ""
    playlistId = 0

    discription = ""
    collaboration = False

    def __init__(self, name):
        sql = "SELECT id FROM Playlist WHERE name=?"
        plId = DBQuery.getOne(sql, name)
        
        if plId == None:
            sql = "INSERT INTO Playlist (name) values (?)"
            id = DBQuery.create(sql, (name,))
            self.playlistId = id
            self.name = name
        else:
            self.playlistId = plId[0]

    def getId(self):
        return self.playlistId

    def getName(self):
        return self.name

    def addSong(self, id):
        if id in self.getSongs():
            return
        sql = "INSERT INTO Playlist2Song VALUES (?,?)"
        DBQuery.executeSql(sql, (self.playlistId, id))      


    def addSongs(self, ids):
        for id in ids:
            if id in self.getSongs():
                continue
            sql = "INSERT INTO Playlist2Song VALUES (?,?)"
            DBQuery.executeSql(sql, (self.playlistId, id))  

    def deleteSong(self, id):
        if id not in self.getSongs():
            return
        sql = "DELETE FROM Playlist2Song WHERE playlistId=? AND song=?"
        DBQuery.executeSql(sql, (self.playlistId, id))
    
    def setCollaboration (self, setCollab):

        self.collaboration = setCollab

    def getCollaboration (self):
        return self.collaboration
    
    def getSongs(self):
        songs = []
        sql = "SELECT song FROM Playlist2Song WHERE playlistId=?"       
        result =  (DBQuery.getList(sql, self.playlistId))
        for song in result:
            songs.append(song[0])
        songs = list(set(songs))
        return songs
        
    
    def setDiscription (self, text):
        self.description = text

    def getDiscription (self):
        return self.description
