#입력
baseValue = float(input("기본 값을 입력하세요: "))
operation = int(input("1. 더하기\n2. 빼기\n3. 곱하기\n4. 나누기\n선택: "))
calculateValue = int(input("숫자 입력: "))




#사칙연산 함수
def selectOperation():
    global baseValue #전역 변수 호출
    if operation == 1: #더하기 일경우
        baseValue += calculateValue
        print("연산 결과: ",baseValue)
    elif operation == 2: #빼기일 경우
        baseValue -= calculateValue
        print("연산 결과: ",baseValue)   
    elif operation == 3: #곱하기 일 경우
        baseValue *= calculateValue
        print("연산 결과: ",baseValue)
    elif operation == 4: #나누기 일 경우
        if calculateValue == 0: #나눗셈 분모가 0일경우
            print("에러: 0으로 나눌 수 없습니다.")
        else:
            baseValue /= calculateValue
            print("연산 결과: ",baseValue)
    else:
        print("올바르지 않은 선택값입니다.")
#함수 실행
selectOperation()