
# 1~100 사이 소수의 값 구하기

sum=2

for i in range(3,101):
    for n in range(2,i):
        if(i % n== 0):
            break
        if(n == (i-1)): #자기자신을 나눌 필요가 없으니깐 17전까지만.
            sum += i
                     
print(sum)