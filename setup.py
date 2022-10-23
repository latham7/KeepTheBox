# Vegetable Development - https://github.com/Vegetable8
# This is to setup parts of KeepTheBox Assistant Server. 

# Imports
import sqlite3

## Vars
con = sqlite3.connect('database.db', check_same_thread=False)

# DB Init
try:
    con.execute("create table Users(username varchar(64),password varchar(64));")
except:
    print("Error - setup.py - Database is already initialized.")


