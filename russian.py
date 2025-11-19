import random

bullet = random.randint(0, 2)  # 3칸 중 한 칸에 탄
print("러시안룰렛 시작 (스페이스 누르고 엔터)")

while True:
    key = input()  # 스페이스+엔터 누르면 발사
    if key == " ":
        if bullet == 0:
            print("빵!!!")
            break
        else:
            print("삑,,,")
            bullet -= 1
