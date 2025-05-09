import random

guess = random.randint(1,100)

while True:
    a = int(input("1부터 100 사이의 숫자를 맞춰보세요 : "))
    if guess == a:
        print("정답입니다 !")
        break
    elif guess < a:
        print("더 작은 숫자입니다.")
    else:
        print("더 큰 숫자 입니다.")