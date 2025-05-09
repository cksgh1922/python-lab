#총 사용자 수 입력받기
#각 사용자에게 초기 10만원 주어짐.
#한 명이 여러번 인출 시도 -> while문
#인출은 정해진단위로만 가능, 이외단위입력시 에러
#잔액보다 큰 금액입력시 잔액부족
#0을 입력하면인출 종료후다음 사용자로 이동
# 잔액이 0이되면 종료
#지정한 사용자 수만큼인출 완료되면 종료


#사용자 수 입력받기
total_user = int(input("총 사용자 수를 입력하세요: "))

#사용자 수만큼for문 반복
for i in range(1,total_user+1):
    #사용자 돈 변수 선언
    money = 100000
    #몇번째 사용자인지 출력하고 초기 잔액도 출력
    print(f"[ {i}번째 사용자 ] 초기 잔액 : {money}원")
    #while문 실행, -> 돈이 0이 아닐 경우 계속해서 반복
    while not money == 0:
        #현재 잔액 출력
        print(f"현재 잔액 : {money}원")
        #인출 할 금액 입력 받기
        input_money = int(input("인출할 금액을 입력하세요. ( 0입력 시 종료 ) : "))
        #입력이 0일시 while문 종료하는 if문 작성
        if input_money == 0:
            print(f"{i}번 사용자 인출이 종료되었습니다.")
            break
        #만약 입력된 인출 금액이 유효하지 않다면 오류 출력
        if input_money != 50000 and input_money != 10000 and input_money != 5000 and input_money != 1000:
            print("인출 단위는 50,000 / 10,000 / 5,000 / 1,000원만 가능합니다.")
        #만약 입력된 인출 금액이 잔액보다 크다면 오류 출력
        elif input_money > money:
            print("잔액이 부족합니다.")
        #아니라면 정상적으로 인출 출력, 총액에서 입력된 값만큼 감소후 값 저장
        else:
            print(f"출금 완료 : {input_money}원")
            money = money - input_money
        
        if money == 0:
            print("잔액이 모두 소진되었습니다.")
            print(f"{i}번 사용자의 인출이 종료되었습니다.")
print()
print("모든 사용자의 인출이 완료되었습니다. 프로그램을 종료합니다.")