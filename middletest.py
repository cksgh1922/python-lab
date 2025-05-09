while True:
    print('''
          ---메뉴---
          1.합계
          2.평균
          3.지수
          4.종료료
          ''')

    input_num = int(input())

    if input_num == 1:
        input_num1 = int(input("첫번째 정수 :"))
        input_num2 = int(input("두번째 정수 :"))
        print(f"합계 : {input_num1+input_num2}")
    elif input_num == 2:
        input_num1 = float(input("첫번째 실수"))
        input_num2 = float(input("두번째 실수"))
        input_num3 = float(input("세번째 실수"))
        print(f"평균 : {(input_num1+input_num2+input_num3)/3}")
    elif input_num == 3:
        input_num1 = int(input("밑수 : "))
        input_num2 = int(input("지수 : "))
        print(f"제곱 : {input_num1**input_num2}")
    elif input_num == 4:
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다.")