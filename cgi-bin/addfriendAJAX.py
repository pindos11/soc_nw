#!/usr/bin/env python3
import cgitb
cgitb.enable()
import time,sys,cgi,sqlite3,codecs
names = cgi.FieldStorage()['usr'].value.split('^^')

db = sqlite3.connect('users.db')
cur = db.cursor()
try:#if this user already has friends it adds to his list one more
    cur.execute('SELECT friends FROM friends WHERE name =?',(names[0],))
    fds = cur.fetchone()[0]
    fds+='^^'+names[1]
    cur.execute('UPDATE friends SET friends =? WHERE name =?',(fds,names[0]))
except:#if user does not have a friend it creates entry with friendlist of this user
    cur.execute('INSERT INTO friends VALUES (?,?)',(names[0],names[1]))


db.commit()
db.close()