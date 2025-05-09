#리스트에 항목 추가하기.

#리스트변수 선언
books = []

#입력 받기
while True:
    title = input("도서 제목을 입력하세요. (종료하려면 '종료' 입력): ")
    if title == '종료': # 종료 입력 시 반복문 종료
        break
    else:
        books.append(title)


#도서 목록 출력
print("도서 목록: ",books)
    