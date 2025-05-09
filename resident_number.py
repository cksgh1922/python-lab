#주민번호 유효성 검사..

#유효 주민등록번호 검사 함수
def resident_or_not():
    #주민번호 계산을 위한 지역 변수 선언 및 값 할당
    total = 0 #유효성 검사 계산식에 사용할 모든 곱의 합
    repeat = 2 #2부터 9까지, 2부터 6까지 곱하기 위한 변수 선언
    #주민번호 길이만큼 반복
    for i in range(13):
        if resident_number[i] == '-': # 하이푼을 걸러내는 조건문
            continue
            #계산식을 위한 total값 구하기
            # 숫자가 9 위로 넘어가면 10이 아니라 2로 변경하는 조건문
        if repeat > 9:
            repeat = 2
        total += int(resident_number[i])*repeat # 입력받은 주민번호 첫 번째 자리부터 끝까지 repeat(2,9)를 곱한값을 total에 저장
        repeat += 1  # 2-9까지 차례대로 곱함
    #검사 계산법 시행 후 값을 저장
    check = (11 - (total%11)) % 10
    #주민등록번호가 유효한지 확인하는 조건문
    if check == int(resident_number[-1]): #check값이 주민번호 마지막 자리랑 같은지 확인
        print("유효한 주민번호입니다.") #맞을 경우
    else:
        print("유효하지 않은 주민번호입니다.") #아닐 경우

#주민번호 입력
resident_number = input("주민번호를 입력하세요: ")

#함수 실행 및 출력
resident_or_not()

