import random
#반복 확인을 위한 리스트 선언
exist_list = []
#행과 열 알고리즘 함수
def table_print(row,col,opt,upgrade_option):
    #옵션 1 선택 시, 테이블 마다 1부터 반복할 변수 선언
    a = 1
    for row_num in range(row):
        for col_num in range(col):
            #선택 1일 경우 함수 호출 및 변수 값 1씩 증가
            if opt == 1:
                #1씩 차례대로 증가하는 a 변수와 두 번째 옵션을 위해 필요한 인자값들을 함수로 전달
                col_print(a,upgrade_option,col_num,row_num,col,row)
                a += 1
            #선택이 2일 경우 랜덤 정수를 생성하여 함수 호출
            else:
                #중복을 검사하는 반복문
                while True:
                    #while문 break를 위한 exist 변수 선언
                    exist = False
                    #랜덤 정수 생성 후 a 변수에 할당
                    a = random.randint(1,100)
                    #중복 검증을 위해 선언했던 list의 길이만큼 반복하는 반복문
                    for i in range(len(exist_list)):
                        #랜덤한 정수 a값이 이미 중복 리스트에 존재한다면 exist변수를 True로 바꾸고, 중복 비교 반복문 종료 후 랜덤 정수 다시 생성
                        if a == exist_list[i]:
                            exist = True
                            break
                    #만약 exist가 False값일 경우, 중복되는 정수가 중복 리스트에 없었다는 뜻이므로, 중복 정수리스트에 추가하고, while문 종료
                    if not exist:
                        exist_list.append(a)
                        break
                #중복되지 않은 정수가 랜덤으로 할당 된 a값과 두 번째 옵션을 위한 필요한 인자값들을 함수로 전달
                col_print(a,upgrade_option,col_num,row_num,col,row)
        print()
#두 번째 옵션 함수
def col_print(a,upgrade_option,col_num,row_num,col,row):
    #테두리 출력 알고리즘
    if upgrade_option == 1:
        #첫번째 열일 경우 모두 행 모두 출력
        if row_num == 0:
            print(a,end=" ")
        #n번째 열이 열의 값에서 1뺀 값과 같다면 ( 0부터 반복 ) 출력
        elif row_num == row-1:
            print(a,end=" ")
        #위 조건이 아닐경우
        else:
            # n번째 열이 0이거나 (첫 번째) 입력받은 행값에서 1뺀 값과 같다면 ( 0부터 반복 )
            if col_num == 0 or col_num == col-1:
                print(a,end=" ")
            # 그게 아니라면 * 출력
            else:
                print("*",end=" ")
    #왼쪽 대각선 알고리즘
    elif upgrade_option == 2:
        #n번째 행과 n번째 열이 같을 때만 출력
        if col_num == row_num:
            print(a,end=" ")
        #아닐 시는 *출력
        else:
            print("*",end=" ")
    #오른쪽 대각선 알고리즘
    elif upgrade_option == 3:
        #n번째 행값에서 n번째 열값을 더한 값이 입력받은 행값과 같다면 출력
        if row_num + col_num == col-1:
            print(a,end=" ")
        #그게 아닐경우
        else:
            print("*",end=" ")
    #양방향 대각선 알고리즘
    else:
        #n번 째 행과 n번째 열이 같거나, n번째 행값에서 n번째 열값을 뺀 값이 입력받은 행값과 같다면 출력
        if row_num + col_num == col-1 or col_num == row_num:
            print(a,end=" ")
        #그게 아니라면 *출력
        else:
            print("*",end=" ")
        
#테이블, 행,열 갯수 입력 받기
table = int(input("테이블 개수 입력 : "))
row = int(input("행 수 입력 : "))
column = int(input("열 수 입력 : "))


while True:
    #출력 옵션 출력 후 옵션 입력 받기
    option = int(input('''
출력 옵션을 선택하세요 :
1. 1부터 시작하여 열 방향으로 증가
2. 1~100사이 랜덤 값 출력
옵션 (1 또는 2): '''))
    if not 1 <= option <= 2:
        print("올바르지 않은 입력입니다.")
    else:
        break

while True:
    upgrade_option = int(input('''
추가 옵션을 선택하세요 :
1. 테두리
2. 왼쪽->오른쪽 대각선
3. 오른쪽 -> 왼쪽 대각선
4. 양방향 대각선
옵션 (1~4) : '''))
    if not 1 <= upgrade_option <= 4:
        print("올바르지 않은 입력입니다.")
    else:
        break
#입력받은 table 값 만큼 반복하여 테이블 출력하며, 행과 열을 출력하는 함수 호출
for i in range(table):
    print(f"테이블 {i+1}")
    table_print(row,column,option,upgrade_option)
    #테이블 마다 줄 구분을 위한 공백 출력
    print()