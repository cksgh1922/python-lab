#문자열
myString = "It is a great weather with you"
#문자열 카운트를 위한 카운트 생성
count = 0
#문자열을 띄어쓰기 기준으로 저장할 변수
sentence = ""
#문자열 반복문
for char in myString:
    #만약 공백이 아닐 경우 문자를 sentence에 넣기
    if char != " ":
        sentence += char
    #만약 공백이면서 sentence에 값이 존재할경우 단어 카운트를늘리고 리스트 초기화
    elif char == " " and sentence:
        count += 1
        sentence = ""
#마지막에 공백이 안들어오고 , 문자열변수에 값이 존재한다면 카운트 늘리기기
if sentence:
    count += 1
    
#출력
print(count) 