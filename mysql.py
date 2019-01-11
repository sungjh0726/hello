import sqlite3
import random
   
fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

addr_city = list("'서울시','수원시','용인시'")
addr_gu = list("'강북구','도봉구','강남구','영통구','기흥구','처인구','수지구'")
addr_dong = list("'미아동','방학동','대치동','신갈동','고덕동','상현동'")

num_list = ('1','2','3','4','5','6','7','8','9') * 4

# x = random.choices(first_names, k = 2)
# print(x, type(x))
y = random.sample(first_names, 2)
print(y, type(y), ''.join(y))

def make_name():
    sung = random.choice(fam_names)
    name = random.sample(first_names, 2)
    return sung, name

def addr():
    city = "".join.random.choice(addr_city)
    gu = "".join.random.choice(addr_gu)
    dong = "",join.random.choice(addr_dong)
    return city, gu, dong

def birth
    year = "".join.random.sample(1950-2003) 
    month = "".join.random.sample(1-12)
    day = "".join.random.sample(1-31)
    for i in range(13)
    for i in range(29)

def tel
    tel_number = (num_list + num_list)
   
def email


conn = sqlite3.connect("t.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values(?)"

    p = ('김일수',)
    print(type(p))
    # cur.execute(sql, ['김일수'])
    cur.execute(sql, p)

    conn.commit()
