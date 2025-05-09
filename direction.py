'''
 up , down, left, right 중 하나를 입력 받아
 입력 받은 문자열에 따라 "왼쪽으로 이동합니다."
 "오른쪽으로 이동합니다", "아래로 이동합니다","위로 이동합니다"
 를 출력하는 프로그램을 작성
 만약 다른 단어가 입력되면 "알 수없는 명령입니다"를 출력하세요
'''
#방향을 입력 받기
direction = input("방향을 입력하세요((left, right, up, down)): ")
#입력받은 방향값 구별하는 조건문
if direction == 'left': # 입력값이 left일 경우
    print("왼쪽으로 이동합니다.") # 왼쪽으로 이동합니다 를 출력
elif direction == 'right': # 입력값이 right일 경우
    print("오른쪽으로 이동합니다.") # 오른쪽으로 이동합니다 를 출력
elif direction == 'up': # 입력값이 up일 경우
    print("위로 이동합니다.") #위로 이동합니다 를 출력
elif direction == 'down': # 입력값이 down일 경우
    print("아래로 이동합니다.") #아래로 이동합니다 를 출력
else: # 아무데도 해당하지 않을 경우
    print("알 수 없는 명령입니다.") #알 수 없는 명령입니다 를 출력