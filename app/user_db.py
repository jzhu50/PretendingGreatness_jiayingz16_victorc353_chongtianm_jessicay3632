# PretendingGreatness: Michelle, Victor, Mark, Jessica
# P4: Makers Makin' It, Act II -- The Seequel
# SoftDev
# March 2025

import sqlite3

user_db = "user.db"

def createUsers():
    users = sqlite3.connect(user_db)
    c = users.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    users.commit()
    users.close()

def addUser(username, password):
    users = sqlite3.connect(user_db)
    c = users.cursor()
    if c.execute("SELECT 1 FROM users WHERE username=?", (username,)).fetchone() is None:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        users.commit()
        users.close()
        return None # success
    users.close()
    return "Username already exists"

def checkPass(username, password):
    users = sqlite3.connect(user_db)
    c = users.cursor()
    pswd = c.execute("SELECT password FROM users WHERE username=?", (username,)).fetchone()
    if pswd is None:
        return "Username doesn't exist. Please register."
    if password == pswd[0]:
        return None
    return "Invalid password. Please try again."