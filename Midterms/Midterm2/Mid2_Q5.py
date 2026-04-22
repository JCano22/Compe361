# 5. Suppose the following table named `Purchases` exists in database `Shop.db` :

# PurchaseID    Material    Price    Quantity    PurchaseDate
# 1001        Whiteboard    150    3        2023-11-01
# 1002        Chair        75    4        2023-11-02
# 1003        Desk        80    7        2023-11-03
# 1004        Blackboard    200    2        2023-11-04

# Write a Python application, which will connect to database Shop.db, retrieve all rows from table `Purchases` and for each row will print: Material, PurchaseDate and Cost (which should be  calculated as multiplication of price and quantity).

import sqlite3
conn = sqlite3.connect("/Users/jorgecano/Desktop/Shop.db")

c = conn.cursor()
c.execute("SELECT * FROM Purchases")

r = c.fetchone()

while r is not None:
    print(r[1] + " " + r[4] + " " + str(r[2] * r[3]))
    r = c.fetchone()

conn.close()