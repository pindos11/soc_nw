#!/usr/bin/env python3
import cgitb
cgitb.enable()
import time,sys,cgi,sqlite3,codecs

names = cgi.FieldStorage()['name'].value.split('^^')

print ("Content-type: text/html;charset=windows-1251")
print ()
#print(names)
db = sqlite3.connect('users.db')
cur = db.cursor()

for msg in cur.execute('SELECT * FROM messages'):
    if((msg[0]==names[0] and msg[1]==names[1])):
        print('<div class = "o_msg">Вы: '+msg[2]+'<br></div>')#writes from or to - whom each message is
    elif((msg[0]==names[1] and msg[1]==names[0])):
        print('<div class = "i_msg">Вам: '+msg[2]+'<br></div>')


#zname = ' '.join(cur.fetchone())
db.close()
#print (zname)
#print(z)