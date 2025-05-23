import random

#입력문
n = int(input("난수 개수를 입력하세요: "))
start = int(input("시작 범위를 입력하세요 : "))
end = int(input("끝 범위를 입력하세요 : "))

#랜덤 숫자를 난수 개수만큼 생성하여 리스트에 추가
random_numlist = []
for i in range(n):
    random_numlist.append(random.randint(start,end))

#중복 제거 한 리스트
num_list = []
for char in random_numlist:
    if char not in num_list:
        num_list.append(char)

#num list 길이만큼 카운트 리스트 생성 후, 카운트 추가
count_list = [0]*len(num_list)
#num list의 i번째 값과 origin_num_list의 전체 값을 비교

for i in range(len(num_list)):
    for num in random_numlist:
        #같을 때마다 count_list[i]번째에 카운트 1씩 증가
        if num == num_list[i]:
            count_list[i] += 1

#출력문
print(random_numlist)
print(f"""
고유 숫자 리스트 : {num_list}
빈도 수 리스트 : {count_list}
""")

# 중복 제거 빈도 리스트
unique_freqs = []
for freq in count_list:
    if freq not in unique_freqs:
        unique_freqs.append(freq)

# 내림차순으로 빈도수 뽑기 (max 없이 직접 수작업)
sorted_freqs = []
while unique_freqs:
    temp_max = unique_freqs[0]
    for val in unique_freqs:
        if val > temp_max:
            temp_max = val
    sorted_freqs.append(temp_max)
    unique_freqs.remove(temp_max)

# 숫자 누적 출력
result_freqs = []  # 출력할 빈도수들
count_numbers = 0  # 출력할 숫자 총 개수

for freq in sorted_freqs:
    # 이 빈도수 freq를 가진 숫자가 몇 개인지 세기
    how_many = count_list.count(freq)
    # 숫자 개수 누적
    count_numbers += how_many
    # 빈도수 리스트에 추가
    result_freqs.append(freq)
    # 총 숫자가 3 이상이면 멈춤
    if count_numbers >= 3:
        break

# 출력
print("가장 많이 등장한 숫자 Top 3 (동점 포함):")
for freq in result_freqs:
    for idx, f in enumerate(count_list):
        if f == freq:
            print(f"숫자 {num_list[idx]}: {f}회")
