ID = "admin"
PASS = "12345"
chance = 5
#아이디는 맞는데 비번 3회 연속 오류 시, 비밀번호 재설정 출력 후 프로그램 종료
PASS_chance = 0
while True:
    #5번 이상 했으면 프로그램 종료
    if chance == 0:
        print("계정이 잠금 되었습니다.")
        break
    if PASS_chance == 3:
        print("비밀번호를 재설정하세요.")
        break
    #아이디와 비밀번호 입력받기
    ID_input = input("ID를 입력하세요: ")
    PASS_input = input("비밀번호를 입력하세요: ")
    #아이디랑 비번맞으면 로그인성공 출력
    if ID_input == ID and PASS_input == PASS:
        print("로그인 성공!")
        break
    #아이디나 비번 둘 중 하나가 틀린 경우
    else:
        #아이디가 맞지 않으면 등록되지 않은 아이디랑 남은 횟수 출력 후 chance -1과 비밀번호 카운트 초기화화
        if ID_input != ID:
            PASS_chance = 0
            chance -= 1
            print(f"등록되지 않은 ID입니다. (남은 시도 {chance}회)")
        #비밀번호가 맞지 않으면 비밀번호 오류랑 남은 횟수 출력 후 chance -1
        elif ID_input == ID and PASS_input != PASS:
            chance -= 1
            PASS_chance += 1
            print(f"비밀번호 오류입니다. (남은 시도 {chance}회)")



