import random
#1부터 100사이 랜덤 정수 생성하여 answear 변수에 저장
answear = random.randint(1,100)
#맞출 때 까지 반복문 시작
while True:
    #정답 입력받기
    user_input = int(input("1부터 100 사이의 숫자를 맞춰보세요 : "))
    #입력받은 숫자가 정답일 경우 정답 출력 후 break로 반복문 종료
    if user_input == answear:
        print("정답입니다!")
        break
    #입력받은 숫자가 정답보다 작을 경우 더 큰 숫자라고 출력
    if user_input < answear:
        print("더 큰 숫자입니다.")
    #입력받은 숫자가 정답보다 클 경우 더 작은 숫자라고 출력
    else:
        print("더 작은 숫자입니다.")
    