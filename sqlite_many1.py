#import sqlite3
import random

#conn = sqlite3.connect("./db/test.db")
fam_names = list("성")
first_names = list("건성현욱정민현주희진김이박최강고윤엄한배성백전황서천방지마피영래주동혜도모영진선재현호시우인성마무병별솔하라")


name = list()

for i in range(100):
    sung = random.choice(fam_names)
    a = random.choice(first_names)
    b = random.choice(first_names)
    name.append(sung + a + b)

#  insert into Student(name) values()

data = tuple(name)
print(data)



# with conn:
#     cur = conn.cursor()
#     sql = "insert into tt(id, name) values(?,?)"
#     cur.executemany(sql, data)

#     conn.commit()
