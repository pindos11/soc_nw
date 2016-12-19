#!/usr/bin/env python3
import cgitb
cgitb.enable()
import time,sys,cgi,sqlite3,codecs

names = cgi.FieldStorage()['msg'].value.split('^^')

#print ("Content-type: text/html;charset=windows-1251")
#print ()
#print(names)
db = sqlite3.connect('users.db')
cur = db.cursor()
inp = (names[0],names[1],names[2])
cur.execute('INSERT INTO messages VALUES (?,?,?)',inp)#just saves everything to batabase
db.commit()
db.close()
