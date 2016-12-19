#!/usr/bin/env python3



print("Content-type: text/html;")
print()
from defines import *
import os,http.cookies,sys



cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
username = cookie.get('name')
if(username!=None):
    print(make_news_page(username.value))
else:
    print(make_login_page(1))


