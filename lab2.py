#while 문을 위한 count변수 선언
count = 0
#3의 배수 총합을 위한 sum 변수 선언
sum = 0
#count가 1000보다 작을 경우 계속해서 반복하는 while문
while count <= 1000:
    #count가 3의 배수일 경우, sum함수에 더하기
    if count % 3 == 0:
        sum += count
    #반복마다 count 1씩 증가
    count += 1
#출력
print(sum)