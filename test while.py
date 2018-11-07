i, sum = 0,0
while (i>=0):
    i += 1

    if (i % 2 == 1):
        sum += i

    if (i==100):
        print (sum)
        break

sum = 0
for i in range(1,101):

    if(1%2==0):
            continue

    sum += 1
    
print(sum)

