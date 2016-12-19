#!/usr/bin/env python3

import cgitb
cgitb.enable()
import time,sys,cgi,sqlite3,codecs

name = cgi.FieldStorage()['name'].value

print ("Content-type: text/html;charset=windows-1251")
print ()
#print(name)
db = sqlite3.connect('users.db')
cur = db.cursor()
cur.execute('SELECT fname,sname,sex FROM users WHERE name =?',(name,))
zname = ' '.join(cur.fetchone())#just sends all, except for password, divided with space
db.close()
print (zname)


