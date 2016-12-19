#!/usr/bin/env python3
import sqlite3
conn = sqlite3.connect('users.db')

cur = conn.cursor()
cur.execute('''CREATE TABLE users (name text, pwd text, fname text, sname text, sex text)''')

cur.execute("INSERT INTO users VALUES ('azudilow','121212','Андрей','Зудилов','male')")
cur.execute("INSERT INTO users VALUES ('I_IVANOV','121212','Иван','Иванов','male')")

cur.execute('''CREATE TABLE messages(name text, name_t text, content text)''')

cur.execute('''CREATE TABLE news(author text, content text, picrel blob,added integer)''')

cur.execute('''CREATE TABLE friends(name text, friends text)''')

conn.commit()
conn.close()

