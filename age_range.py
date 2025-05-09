#입력 받은 나이값에따라 청소년(Teenager),성인(adult),노년(Senior)
#중 하나로 분류하는 프로그램 작성

#사용자로부터 나이 입력받기
age = int(input("나이를 입력하세요: "))

#나이를 분류하는 조건문 시작
if 13<= age <= 19: #입력된 나이가 13이상 19이하일 경우
    print("You are in the 'Teenager' age group.") #'Teenager'를 출력
elif 20 <= age <= 64: #입력된 나이가 20이상 64이하일 경우
    print("You are in the 'Adult' age group.") #'Adult'를 출력
elif age >= 65: #입력된 나이가 65 이상일 경우
    print("You are in the 'Senior' age group.") #'Senior'를 출력
else: #입력된 나이가 어디에도 포함되지 않을 경우
    print("You are in the 'Unknown age group'") #'Unknown age group'을 출력