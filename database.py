import sqlite3

con = sqlite3.connect('database.db', check_same_thread=False)

def initDb():
    try:
        con.execute("create table Users(username varchar(64),password varchar(64));")
        return
    except:
        print("DB Already Initialized.")


def createUser(username,password):
    con.execute(f"INSERT INTO Users(username,password) VALUES ('{ username }','{ password }');")
    con.commit()
    return


