import sqlite3
from flask import render_template, request

con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

def checkAuth(username, password):
    cur.execute(f"SELECT * FROM Users WHERE username='{username}' AND password='{password}'")
    stored = cur.fetchall()
    print(stored)
    print(f"[('{ username }', '{ password }')]")
    try :
        if stored[0][0] == username:
            if stored[0][1] == password:
                return True
        else:
            return False
    except:
        print("Error - auth.py - CheckAuth function")
#    try:
#        con.execute(f"SELECT * FROM Users WHERE username='{ username }' AND password='{password}'")
#        return True
#    except:
#        return False


def checkCookie(cookie):
    try:
        con.execute(f"SELECT * FROM Users WHERE username='{cookie}''")
        return True
    except:
        return False


