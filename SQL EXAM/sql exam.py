import sqlite3
 
conn = sqlite3.connect("students.db")
 
with conn:
    cur = conn.cursor()
    sql = "select * from Student where id=? or name=? or grade=? or addr=? or gender=? or age=?"
    cur.execute(sql, (1, ''))
    rows = cur.fetchall()
 

 with open("./students.csv", "r", encoding="utf-8")
    for line in file:
        print(line.strip())


g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()

class Students:
    grade = ''

    def __init__(self, line):
        id, name, grade, addr = line.strip().split(',')
        self.id = id
        self.name = name
        self.grade = grade
        self.addr = addr
        self.gender = gender
        self.age = age

    def __str__(self):
        return "{}\t{}**\t{}\t{}\t{}".format(self.id self.name[0], self.grade, self.addr self.gender self.age)

    def make_grade(self):
        if self.score == 100:
            self.grade = 'A+'
        elif self.score < 50:
            self.grade = 'F'
        else:
            self.grade = g_grades[self.score // 10 - 5]

    def gender
    if gender(list_elemnet) =="남":
        return list_elemnet = M 
    else gender(list_elemnet)  == "여":
        return list_elemnet = F

    def age
     if age[] = int(20~29):
         return age = 20대

     elif age[] = int(30~39):
         return age = 30대
     
     elif age[] = int(40~49):
         return age = 40대
     
     elif age[] = int(50~59):
         return age = 50대
     
     elif age[] = int(60~69):
         return age = 60대
     
     elif age[] = int(70~79):
         return age = 70대
     
     else:
          age[] = int(80~89)
         return age = 80대
     
def addr 

 with open 
    for row in rows:
        print(row)