#리스트에서 항목 읽기

#리스트 정의
menus = ["피자","파스타","샐러드","스시","버거"]

#인덱스 입력받기
index = int(input("메뉴의 인덱스를 선택하세요 (0부터 시작): "))

#조건문 작성
if index < 0 or index >= len(menus):
    print("유효하지 않은 선택입니다.")
else:
    print("선택된 메뉴: ", menus[index])
