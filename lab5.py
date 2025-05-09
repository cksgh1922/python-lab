# 점수 입력
score = [99,29,30,40,20,60]
# 총합을 저장할 sum 변수 선언
sum = 0
# 학생 수를 저장할 student_num 변수 선언
student_num = 0
# 평균을 저장할 avg 변수 선언
avg = 0
#score 리스트에 대한 반복문 시작
for item in score:
    #저장된 정수형 아이템을 sum 변수에 더하기
    sum += item
    #반복할 때마다 학생 수 카운트 1씩 증가하기기
    student_num += 1
#반복문을 통해 구한 총합(sum)을 학생수(student_num)으로 나눠서 avg 변수에 저장
avg = sum / student_num
#출력문
print(f"학생 수 : {student_num} , 총점 : {sum}, 평균 : {avg}")