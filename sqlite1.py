import sqlite3
import random


conn = sqlite3.connect('test.db')

cur = conn.cursor()

cur.execute("select * from Student")

rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()