#1부터 20까지의 수 중에, 짝수의 합계를 저장할 sum 변수선언
sum = 0
#1,20까지 반복하는 for문
for i in range(1,21):
    #만약 홀수라면 continue로 건너뛰기
    if i % 2 != 0:
        continue
    #1,20까지 수 중에, 짝수일 경우 sum에 추가
    sum += i
#출력
print(sum)

# #1부터 20까지의 수 중에, 짝수의 합계를 저장할 sum 변수선언
# sum = 0
# #while문을 위한 count변수 선언
# count = 1
# #1,20까지 반복하는 while문
# while count <= 20:
#     #만약 홀수라면 continue로 밑에 코드 실행 X
#     if count % 2 != 0:
#         count += 1
#         continue
#     #짝수면 sum에 count 추가
#     sum += count
#     #count변수 1 증가
#     count+=1

# print(sum)