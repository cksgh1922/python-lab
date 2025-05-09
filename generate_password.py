#패스워드생성기

import random

#패스워드 생성 함수
def generate_password():
    #대문자,소문자,숫자를 포함한문자
    uppercase_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letter = uppercase_letter.lower() #대문자 -> 소문자 변환
    digits = '0123456789' #숫자
    all_char = uppercase_letter + lowercase_letter + digits # 대소문자 결합

    global password
    
    for char in range(length): #지정된 길이만큼 랜덤 문자선택
        password += random.choice(all_char) #랜덤 문자를 패스워드에 추가
    
    #패스워드변환환
    return password

#입력
length = int(input("패스워드 길이를 입력하세요. "))

#함수 호출 및 출력
#패스워드 초기화
password = ""
generate_password()
print(f"생성된 비밀번호는 {password}입니다.")


# 다시 풀어보기. key포인트 for char. if char 도 인지지