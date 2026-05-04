#5.    Write a Python application that retrieves rows from the `StudentProfile` table in the University.db database.
import sqlite3

con = sqlite3.connect('final5.db')

cmd1 = con.cursor()
cmd2 = con.cursor()

cmd1.execute("SELECT * FROM StudentProfile")

r = cmd1.fetchone()

while r != None:
    cmd2.execute("SELECT * FROM StudentProfile WHERE id=?", (r[1],))
    stud = cmd2.fetchone()
    print(str(r[0]) + ", " + stud[1] + " " + stud[2] + ", " + str(r[3]))

con.close()