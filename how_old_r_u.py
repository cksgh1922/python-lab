#현재 연도와 태어난연도를 입력받아 나이 계산

#현재 연도를 입력받는다.
current_year = int(input("현재 연도를 입력하세요 : "))

#태어난 연도를 입력받는다.
born_year = int(input("태어난 연도를 입력하세요 : "))

#현재 연도에서 태어난 연도를 빼서 변수에 저장한다.
age = current_year-born_year

#나이를 출력한다.
print("당신의 나이는 ",age,"살 입니다.")