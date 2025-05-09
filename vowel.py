# 하나의 영문자를 입력받고, 해당 문자가 모음(a,e,i,o,u)중
# 하나인지아닌지 판별하여 결과를 출력하는 프로그램 작성

# 하나의 문자를 입력받기
a = input("한 문자를 입력하세요: ")

# 모음인지 아닌지 확인하는 함수 만들기
def vowel(argValue):
    if argValue in 'aeiuo':
        msg = argValue +"는 모음입니다."
        print(msg)
    else:
        msg = argValue +"는 모음이 아닙니다."
        print(msg)

vowel(a)
