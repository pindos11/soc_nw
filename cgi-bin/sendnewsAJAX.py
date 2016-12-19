#!/usr/bin/env python3
import cgitb,time,binascii,html,urllib
cgitb.enable()
import time,sys,cgi,sqlite3,codecs
form = cgi.FieldStorage()
names = form.getvalue('msg').split('^^')
pict = form.getvalue('pic')
#print ("Content-type: text/html;charset=windows-1251")
#print ()
#print(form)
#print(names)
#a = binascii.a2b_base64(pict)
if(pict!='noimg'):#i thought about converting image somehow on server
    pic = pict
else:
    pic = pict
db = sqlite3.connect('users.db')
cur = db.cursor()
inp = (names[0],names[1],pic,time.time())
cur.execute('INSERT INTO news VALUES (?,?,?,?)',inp)
db.commit()
db.close()
