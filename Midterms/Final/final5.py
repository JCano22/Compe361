#5.    Write a Python application that retrieves rows from the `StudentProfile` table in the University.db database.
import sqlite3
#Grades, Students
con = sqlite3.connect('/Users/jorgecano/Documents/School/Compe361/Midterms/Final/University.db')

cmd1 = con.cursor()
cmd2 = con.cursor()

cmd1.execute("SELECT * FROM Grades")

r = cmd1.fetchone()

while r != None:
    cmd2.execute("SELECT * FROM Students WHERE StudentID = ?", (r[1],))
    stud = cmd2.fetchone()
    print(str(r[0]) + ", " + stud[1] + ", " + r[2] + ", " + str(r[3]))
    r = cmd1.fetchone()

con.close()
