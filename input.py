user_input_msg = input("Input(usage: 이름,나이,성별)>> ") # 1. 입력하라는 함수를 가진 cmd에 값을 입력해라 ->cmd = input("Input(usage: 이름,나이,성별)>> ")
print (cmd) #2. 그리고 이걸 일단 값을 입력하게끔 출력해라

#1. 값의 존재여부 체크
if cmd == ' ':
   print("error_msg")
   exit()


#2. ,가 있는지 없는지
if ',' not in cmd:
    print ("")


#3. 값이 3개인지
if len(cmds) != 3:
     print(error_msg)
     exit()
outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {} 입니다" #3. outmsg는 " 당신의 이름 ----" 이다
cmds = cmd.split (',') #2. 입력된 cmd를 ,로 찢어라 이게 cmds다 ->cmds = cmd.split (',')
print(outmsg.format(cmds[0], cmds[1], cmds[2])) #4. 나온 cmds가 성재현, 12, 남자 이렇게 나오면 이 값들을 outmsg에 넣어라 -> print(outmsg.format(cmds[0], cmds[1], cmds[2]))