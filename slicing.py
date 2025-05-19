#리스트 생성
num_list = []
#정수 10개를 입력받기
for i in range(1,11):
    num_list.append(int(input(f"{i}번째 정수: ")))

#출력문문
print(f"""
[원본 리스트]
{num_list}

1. 처음 5개 원소:
{num_list[:5]}

2. 뒤에서 3개 원소:
{num_list[-3:]}

3. 짝수 인덱스 원소:
{num_list[::2]}

4. 거꾸로 뒤집은 리스트:
{num_list[::-1]}""")