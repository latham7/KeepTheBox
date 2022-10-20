import sqlite3
from flask import request

con = sqlite3.connect('database.db', check_same_thread=False)

def checkAuth(username, password):
    test = con.execute(f"SELECT * FROM Users WHERE username='{username}' AND password='{password}'")
    print(test)
    try:
        con.execute(f"SELECT * FROM Users WHERE username='{ username }' AND password='{password}'")
        return True
    except:
        return False


def checkCookie(cookie):
    try:
        con.execute(f"SELECT * FROM Users WHERE username='{cookie}''")
        return True
    except:
        return False


