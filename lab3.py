#문자열 생성
my_string = "hello hyundai hoho"
#문자열 내 h갯수를 세기위한 count 변수선언
count = 0
#문자열 반복문
for char in my_string:
    #문자열이 h일 경우 카운트 증가
    if char == "h":
        count += 1
#최종 h갯수 출력
print(f"문자열 내 h 갯수 : {count}")