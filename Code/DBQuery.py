import sqlite3

def getOne (sql, id):
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    c.execute(sql, (id,))
    value = c.fetchone()
    conn.close()
    return value

def getList (sql, id):
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    c.execute(sql, (id,))
    list = c.fetchall()
    conn.close()
    return list

def find (sql):
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    c.execute(sql)
    list = c.fetchall()
    conn.close()
    return list

def executeSql(sql, args):
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    c.execute(sql, args)
    conn.commit()
    conn.close()

def create(sql, args):
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    c.execute(sql, args)
    id = c.lastrowid
    conn.commit()
    conn.close()
    return id


