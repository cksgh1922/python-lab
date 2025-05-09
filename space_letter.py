#공백을 기준으로 문자열에서 특정 단어의 출현 빈도 계산하기
import re
#특정단어출현빈도 함수
def check(str):
    #각 문자 순회하며 공백이나 , 을 만나면 그 전까지 문자를 하나의단어로 합체
    word_list = re.split([r'\s,\.!?~'],str)
    print(word_list)
    #리스트에 집어넣기
    #각단어를 추출해 놓은 리스트에서, 입력해 놓은 문자열과 비교
    


# 입력
sentence = input("문자열 입력: ")
word = input("단어 입력: ")

#함수 호출 및 출력
check(sentence)