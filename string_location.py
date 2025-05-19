#미리 정의된 문자열 설정
txt = "apple banana orange apple kiwi apple mango"
#찾을 단어 입력받기
find_word = input("찾을 문자열을 입력하세요: ")
#문자열을 단어로 나눠 저장할 리스트 생성
word_list = []


#단어별로 끊기 위해 변수 생성
word = ""
#문자열 반복문 
for char in txt:
    #공백을 만나면 word에 저장된 단어를 리스트에 저장 후 초기화
    if char == " ":
        word_list.append(word)
        word = ""
    #공백이 아닐경우 word에 문자 계속해서 추가
    else:
        word+= char
#만약 word에 단어가 들어가 있다면 마지막으로 리스트에 추가
if word:
    word_list.append(word)

#찾을 단어 갯수 카운팅 할 count 와 인덱스 위치를 저장할 index_list 리스트 생성
count = 0
index_list = []
#리스트 반복문에서 저장된 단어와 입력 단어가 일치할 때마다 카운트 증가
for i in range(len(word_list)):
    if find_word == word_list[i]:
        count += 1
        index_list.append(i)

#출력문
print(f"'{find_word}'는 총 {count}번 등장합니다.")
print(f"위치 (인덱스): {index_list}")