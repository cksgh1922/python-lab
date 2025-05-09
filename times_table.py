n = int(input("출력할 단을 입력하세요 (2~9) : "))
if n >= 10 or n <= 1:
    print("오류 : 2단부터 9단까지만 입력 가능합니다.")
    exit()
for i in range(2,9,2):
    print(f"{n} X {i} = {n*i}")