from functools import reduce
from Student import Student
# import Student

g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()

students = []
with open('students.csv', 'r', encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue #0번째에 값이 있으면 패스해라
        students.append( Student(line) ) #stdent라는 클래스에 학생정보를 가지고 있는 인자를 줘서 학생하나하나를 인스턴스로 만든다. prothery를 가지고 있는 instance 

students.sort(key = lambda stu: stu.score, reverse = True) #lambda x : x>0
m = map(lambda stu: stu.make_grade(), students)
list(m) 

def sumfn(x, y):
    if type(x) == int:
        return x + y.score
    else:
        return x.score + y.score

# total = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, students)
total = reduce(sumfn, students)
avg = total / len(students)
print("총계, 평균>>>", total, avg)

print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")
for s in students:
    print(s)

print("-----------------------------")
for s in students:
    if s.score >= avg:
        print(s.name, s.score)