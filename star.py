

num = int(input())  # 사용자로부터 숫자를 입력받는다.

# 위 삼각형 출력
for i in range(1, num + 1):  # 1부터 num까지 반복
    print("*" * i)

# 아래 삼각형 출력
for i in range(num-1, 0, -1):  # num-1부터 1까지 반복
    print("*" * i)
