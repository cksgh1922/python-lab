#로그인 시스템 : 사용자가 최대 5번
# 로그신 시도 허용, 올바른 아이디 입력시
#성공 , 5번 실패시, 계정 잠금 메세지 출력

#아이디 비밀번호 사전에입력
ID = "admin"
PW = "1234"
# 카운트 변수 생성 후 5 입력
count = 5
# 카운트 변수가 0이 아니라면 계속해서 반복
while not count == 0:
    #아이디 비밀번호 입력받기
    ID_input = input("ID 입력 : ")
    PW_input = input("PW 입력 : ")
    #아이디, 비밀번호가 사전에 입력된 아이디,비밀번호와 일치한다면 로그인성공 출력후 break로 탈출
    if ID == ID_input and PW == PW_input:
        print("로그인 성공!")
        break
    #아닐경우 카운트 값을 1감소하며 오류메세지 출력 및, 남은 시도 횟수 출력력
    else:
        count -= 1
        print(f"ID 또는 PW가 잘못되었습니다. ( 남은 시도 : {count} )")
#만약 5번 다 실패해서 while문이 종료되었다면 계정잠금 메세지 출력
if count == 0:
    print("계정이 잠금되었습니다.")