class Square:
    x, y =0, 0
    def __init__(self):
        print("Square 만들기")

class Rec(Square)
    def 넓이(self, x, y):
        return x * y

class Parel(Square):
    def 넓이(self, x, y):
        return x * y

rect_type = input("사가곃ㅇ의 종류는?/n 1)직사각형/n 2)평행사변형/n >>")

if rect_type =='1':
    rect1 = Rec
    가로_세로 = input("가로와 세로는 ??(usage: 가로, 세로")
    print"()
    x, y = 가로,세로.split(',')
    결과 = rect1.넓이 (가로, 세로)
    print("직사각형의 넓이는 {}입니다.".format(결과))

else:
    rect_type =='1':
    rect2 = Parel
    밑변_높이 = input("밑변과 높이는 ??(usage: 가로, 세로")
    밑변, 높이 = 밑변_높이.split(',')
    결과 = rect2.넓이 (가로, 세로)
    print("평행사변형의 넓이는 {}입니다.".format(결과))