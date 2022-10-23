import sqlite3
from flask import render_template, request

con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

def checkAuth(username, password):
    cur.execute(f"SELECT * FROM Users WHERE username='{username}' AND password='{password}'")
    stored = cur.fetchall()
    try :
        if stored[0][0] == username:
            if stored[0][1] == password:
                return True
        else:
            return False
    except:
        print("INFO - Incorrect Username or Password")
        print(f"---- {username} - {password}")
#    try:
#        con.execute(f"SELECT * FROM Users WHERE username='{ username }' AND password='{password}'")
#        return True
#    except:
#        return False


def checkCookie(cookie):
    cur.execute(f"SELECT * FROM Users WHERE username='{cookie}'")
    stored = cur.fetchall()
    print(stored)
    try: 
        if stored[0][0] == cookie:
            return True
        else: return True
    except:
        print("Error - auth.py - checkCookie")
        return False

