#야구게임 만들기 
import random
#컴퓨터랑 유저 난수, 입력값 저장할 리스트
computer_sb = []
user_sb = []
strike, ball, out = 0

#겹치지 않는 난수 3개 생성해 computer_sb에 넣기
while len(computer_sb) < 3:
    a = random.randint(0,9)
    if a not in computer_sb:
        computer_sb.append(a)

for i in range(5):
    if 