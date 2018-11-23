shape = ["S", "D", "H", "C"]
number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
point = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
points = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"] * 4

# S2 , 2 

### 카드를 만드는 부분. 그 값은 리스트의 형태로 반환.
### return card자료형... 리스트
# {number :point}
# { } 13개

# card = {}
# card = {number : point}
# print(card)

card = {}
for i in range(13):
    card[number[i]] = point[i]  ## card = { num[i] : potin}
                                ## 딕셔너리 쌍 추가하기 http://mystyle1057.tistory.com/211

print(card)

y = list(card.keys())
print(y)

score = []
for i, j in enumerate(shape):
    for v, w in enumerate(number):
        a = j + w
        score.append(a)

print(score)
cards = {}
for i in range(52):
    cards[score[i]] = points[i]                  

print(cards)