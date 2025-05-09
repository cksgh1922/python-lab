import random
#1부터 100사이 랜덤 정수 생성하여 answear 변수에 저장
answear = random.randint(1,100)
#기회 10번을 주기 위한 chance 변수 선언
chance = 1
#맞출 때 까지 반복문 시작
while True:
    #정답 입력받기
    user_input = int(input(f"기회 {chance}/10 - 1부터 100 사이의 숫자를 맞춰보세요 : "))
    
    #입력받은 숫자가 정답일 경우 정답 출력 후 break로 반복문 종료
    if user_input == answear:
        print("정답입니다!")
        break
    #만약 chance 변수의 값이 10이 넘어가면 답을 알려주고 break를 통해 종료
    if chance >= 10:
        print(f"모든 기회를 사용하였습니다. 정답은 {answear}입니다.")
        break
    #입력받은 숫자가 정답보다 작을 경우 더 큰 숫자라고 출력
    if user_input < answear:
        print("더 큰 숫자입니다.")
        chance += 1
    #입력받은 숫자가 정답보다 클 경우 더 작은 숫자라고 출력
    elif user_input > answear:
        print("더 작은 숫자입니다.")
        chance += 1
    #0을 입력할 경우 break로 반복문 종료
    elif user_input == 0:
        break
print("게임이 끝났습니다.")