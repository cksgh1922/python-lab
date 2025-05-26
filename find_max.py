#입력받기
score = list(map(int,input().split()))

#인덱스 슬라이싱 -> 여기서 새로운 리스트를 생성하여 각 변수에 저장하게 됨.
spring = score[:5]

autumn = score[5:]

max1 = 0
max2 = 0
for num in spring:
    if max1 < num:
        max1 = num

for num in autumn:
    if max2 < num:
        max2 = num
        
print(f"""
1학기 최고 점수 : {max1}
2학기 최고 점수 : {max2}""")