import random

guess = random.randint(1,100)
user = 0
while True:
    if user == 10:
        print(f"모든 기회를 사용하였습니다. 정답은 {guess}입니다.")
        break
    a = int(input(f"기회 {user}/10 - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력) : "))
    if a == 0:
        break
    if guess == a:
        print("정답입니다 !")
        break
    elif guess < a:
        print("더 작은 숫자입니다.")
        user += 1
    else:
        print("더 큰 숫자 입니다.")
        user += 1
print("게임이 끝났습니다.")