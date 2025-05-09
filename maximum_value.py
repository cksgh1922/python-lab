# 정수를 세 개 입력받아 가장 큰 수를 찾기

#큰 숫자 정의하기
max = 0
# 정수를 입력받기
num1 = int(input("첫 번째 숫자를입력하세요: "))
max = num1
num2 = int(input("두 번째 숫자를입력하세요: "))
#만약 첫 번째로 입력받은 수가 두 번째로 받은 수보다 작을 경우
if num2 > max:
    max = num2 #최댓값에 두 번째 숫자 저장
else:
    pass # 그게 아닐시 첫 번째 숫자 유지
num3 = int(input("세 번째 숫자를입력하세요: ")) # 세번째 숫자 입력받기
if num3 > max: #세번째 숫자가 최댓값에 저장되어 있는 수보다 클 경우
    max = num3 # 최댓값에 세번째 숫자 저장
else:
    pass # 아닐 경우 최댓값 유지

#최댓값 출력
print("가장 큰 숫자는 ",max,"입니다.")


'''a = list(map(int,input().split()))
a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
print(a)
print(max(a))
'''