def plus(a, b):
    return a + b
      
def minus(a, b):
    return a - b

def multiple(a, b):
    return a * b

def div(a, b):
    return a / b

{while(true):
q = input("숫자 op 숫자>>> ")

if q == "quit":
    break}

Q = input("수식을 입력하세요(usage: 2 + 3)a op b>>> ")
print(Q)

qs = Q.split(' ')

# a = qs[0]
# op = qs[1]
# b = qs[2]

a, op, b = qs
# print("a=",a, ", op=", op, ", b=", b)

a, b = int(a), int(b)




#outtype = "{:d}"
if op == '+':
    r = plus(a, b)

elif op == '-':
    r = minus(a,b)

elif op =='*':
    r = mul(a, b)

else:
    r = div(a,b)

if op =='/':
    print("answer is {:.2f}".format(r))

else:
    print("anser is {:d}".format(r))


