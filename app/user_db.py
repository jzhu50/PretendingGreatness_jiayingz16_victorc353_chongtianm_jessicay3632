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


