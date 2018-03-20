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
