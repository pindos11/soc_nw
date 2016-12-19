#!/usr/bin/env python3
from defines import *
import cgi
import html,codecs,sqlite3

form = cgi.FieldStorage()
inplogin = form.getfirst("user","none")
inppwd = form.getfirst("pwd","none")
a = 0
z = ''
db = sqlite3.connect('users.db')
cur = db.cursor()
for usr in cur.execute("SELECT name,pwd FROM users"):
    if(usr[0]==inplogin and usr[1]==inppwd):#if login and pass are correct
        print("Set-cookie: name="+inplogin)#sets a cookie until browser is closed
        print("Content-type: text/html;")
        print()
        redir = '''
        <head>
        <script type="text/javascript"> 
            location="index.py";
        </script>
        </head>
        '''
        print(redir)
        a = 1
        break

db.close()
if(a == 0):
    print("Content-type: text/html")
    print()
    print(make_login_page(0))#if not okay - asks to login again
