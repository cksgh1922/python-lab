#나이 제한이 있는 이벤트는 사용자의 나이를 확인하여 조건에 맞지
#않을 경우 "나이제한으로 인해 할 수 없습니다."라고 해야함
#날짜 제한이 있는 이벤트는 사용자가 입력한 날짜를 검증하여 조건에
#맞지 않을경우 "선택하신 날짜에는 예약할 수 없습니다."
#사용자가 입력한 event_code나 reservation_date가 형식에맞지 않을경우
#잘못된 입력입니다. 프로그램을 종료합니다. 라고출력하고 프로그램을 종료

def check_simulation(age,event,day):
    if 1 <= day <= 30: #날짜가 1에서 30일 경우
        if event not in ['E1','E2','E3']:
            return "잘못된 입력입니다. 프로그램을 종료합니다1."
        elif event == 'E1': #E1일 경우
            if age >= 18: #나이가 18세 이상일경우
                return "예약이 완료되었습니다." 
            else: #아닐 경우
                return "나이 제한으로 인해 예약할 수 없습니다."
        elif event == 'E2': #E2일경우
            if day%2 == 0: #날짜가 짝수 일경우
                return "예약이 완료되었습니다." 
            else: # 아닐 경우
                return "선택하신 날짜에는예약할 수 예약할 수 없습니다."
        else: #E3일 경우
            if age >= 16: #나이가 16 이상인경우에서
                if day%7 == 0: #7의 배수인 날짜인경우
                    return "예약이 완료되었습니다."
                else: #7의 배수가아닐 경우
                    return "선택하신 날짜에는 예약할 수 없습니다."
            else: #나이가 16보다 적을 경우
                return "나이 제한으로 인해 예약할 수 없습니다."
    else: #날짜가 1에서 30이 아닐 경우
        return "잘못된 입력입니다. 프로그램을 종료합니다2."

#나이와 이벤트 코드, 날짜 입력받기
age = int(input("나이를 입력하세요: "))
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
reservation_code = int(input("원하는 예약 날짜를 입력하세요: "))

print(check_simulation(age,event_code,reservation_code))
