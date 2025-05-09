#비밀번호가 안전한지 출력 프로그램
def valid_password(password):
    has_uppercase = False
    has_number = False
    length_long = False
    if len(password) < 8:
        return "비밀번호가 짧습니다."
    else:
        length_long = True
    
    for char in password:
        if char.isdigit():
            has_number = True
            break
        
    for char in password:
        if char.isupper():
            has_uppercase = True
            break
    
    if has_uppercase and has_number and length_long :
        return "안전한 비밀번호 입니다."
    elif not has_uppercase and has_number:
        return "비밀번호는 대문자를 포함해야 합니다."
    elif not has_number and has_uppercase:
        return "비밀번호는 숫자를 포함해야 합니다."
    else:
        return "비밀번호는 숫자와 대문자를 포함해야합니다"
                
            
#비밀번호 입력 및 검증 함수 호출 후 출력
password = input("비밀번호를 입력하세요: ")
print(valid_password(password))


# 키포인트 : bool 문법 숙지 if not이나 true false값 생략 등. 
# for char in 도 숙지  -> 문자열 비교
# 새로운 함수 isupper() , isdigit()
