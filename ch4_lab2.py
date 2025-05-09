import random
def random_number(n):
    numbers = set()

    while len(numbers) < n:
        num = random.randint(1,100)
        numbers.add(num)
    
    return list(numbers)

while True:
    a = int(input("N값을 입력하세요 : "))
    if a < 0 or a > 100:
        print("에러 : N은 1이상 100 이하의 정수여야 합니다.")
    else:
        break
random_list = random_number(a)
print("생성된 리스트 : ",*random_list)
while True:
    s = int(input(f"원하는 원소의 인덱스를 입력하세요 (0-{a-1}): "))
    if 0 < s < a-1:
        print("선택한 인덱스의 원소: ",random_list[s])
        break
    else:
        print("에러 : 유호한 인덱스 범위를 벗어났습니다.")