# PretendingGreatness: Michelle, Victor, Mark, Jessica
# P4: Makers Makin' It, Act II -- The Seequel
# SoftDev
# March 2025

import sqlite3

user_file = "user.db"

def createUsers():
    users = sqlite3.connect(user_file)
    c = users.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    users.commit()
    c.close()

def addUser(username, password):
    users = sqlite3.connect(user_file)
    c = users.cursor()
    if c.execute("SELECT 1 FROM users WHERE username=?", (username,)).fetchone() is None:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        users.commit()
        c.close()
    return "Username already exists"

def checkPass(username, password):
    users = sqlite3.connect(user_file)
    c = users.cursor()
    if c.execute("SELECT 1 FROM users WHERE username=?", (username,)).fetchone() is None:
        return "Username doesn't exist. Please register."
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    res = c.fetchone()
    if password == res[0]:
        return None
    return "Invalid password. Please try again."

           