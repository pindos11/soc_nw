#!/usr/bin/env python3
from defines import *
import cgi
import html,codecs,sqlite3

form = cgi.FieldStorage()
inplogin = form.getfirst("user","none")
a = 0
db = sqlite3.connect('users.db')
cur = db.cursor()
for usr in cur.execute("SELECT name FROM users"):
    try:
        if(usr[0]==inplogin):#if there is alreade a user with that login throws out
            a = 1
            break
    except:
        a = 0
if(a == 1):
    print("Content-type: text/html")
    print()
    print(make_reg_page(1))#and says that you need a different login
    db.close()
else:#otherwise just saves all the data to database
    inppwd = form.getfirst("pwd","none")

    inpfname = form.getfirst("fname","Не задано")
    inpsname = form.getfirst("sname","Не задано")

    inpsex = form.getfirst("sex","Не задано")
    tosave = (inplogin,inppwd,inpfname,inpsname,inpsex)
    cur.execute("INSERT INTO users VALUES (?,?,?,?,?)",tosave)

    db.commit()
    db.close()

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
