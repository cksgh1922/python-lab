import random
#입력문
while True:    
    n = int(input("N값을 입력하세요 (1-100) : "))
    if n < 0 or n > 100:
        print("에러 : N은 1 이상 100 이하의 정수여야 합니다.")
    else:
        break
#리스트 선언
rd_list = []
#입력 받은 값만큼 중복되지 않는 랜덤한 정수 생성하여 리스트에 넣는 알고리즘
while len(rd_list) < n:
    a = random.randint(1,n)
    duple = False
    for i in range(len(rd_list)):
        if rd_list[i] == a:
            duple = True
            break
    if not duple:
        rd_list.append(a)
#생성된 리스트 출력
print(f"생성된 리스트 : {rd_list}")
#원하는 원소 인덱스 입력문
while True:
    choice = int(input(f"원하는 원소의 인덱스를입력하세요 : (0-{n-1}): "))
    if choice > n or choice < 0:
        print("에러: 유효한 인덱스 범위를 벗어났습니다.")
    else:
        print(f"선택한 인덱스의 원소 : {rd_list[choice]}")