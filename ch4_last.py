student = {'id' : '', 'name': '', 'kor':0, 'eng':0, 'math':0, 'sum':0, 'avg':0.0}
students = []
student_average = 0

#선택지 출력 함수수
def chat_set():
    print("==========================")
    print("  1.학생 성적 입력")
    print("  2.학생 목록 출력(입력 순)")
    print("  3. 프로그램 종료")
    print("==========================")
    print()
    print(f"현 입력 데이터 갯수 : {len(students)}")
    print(f"전체 학생 평균 값 : {student_average:.2f}")

#평균 계산하는 함수
def sum_avg(kor,eng,math):
    total =  kor + eng + math
    avg = total/3
    return total, avg

#학생 정보 업데이트 함수
def update_student_average():
    global student_average# student_average를 수정하기 위해 global로 전역함수 호출 및 값 변경
    if students:
        student_average = sum([student['avg'] for student in students]) /len(students) # student average 출력을 위해 students내의 student 딕셔너리 에서 avg key의 값을 student의 길이만큼 나눈값을 저장
    else:
        student_average = 0
    
#학생 입력받는 함수
def create_user():
    student = {  #입력받은 정보를 딕셔너리 각 key에 할당
            'id' : input("학번을 입력하세요\n"),
            'name': input("이름을 입력하세요\n"),
            'kor': int(input("국어 성적을 입력하세요\n")),
            'eng': int(input("영어 성적을 입력하세요\n")),
            'math': int(input("수학 성적을 입력하세요\n"))
        }
    student['sum'],student['avg'] = sum_avg(student['kor'],student['eng'],student['math']) #국영수점수를 sum_avg함수를 호출해 총합, 평균 계산하여student sum,avg값에 저장장
    students.append(student) # student 즉 학생의 정보를 , students라는 리스트에 딕셔너리 student를 저장.
    update_student_average() # students내 student의 avg 키를 students len 으로 나눠 student_average에저장.
    
while True: #3을 입력하기 전까지 반복
    chat_set() # 선택지 제공
    selection = int(input()) # 1,2,3 중 하나를 입력받는다.
    if selection == 1: #선택지 1일경우
        create_user() # 학생 추가 함수를 호출해 학생을 입력 받는다
    elif selection == 2: #선택지 2일경우
        if student: #만약 student가 있을경우 ,
            for student in students: #students에 저장된 student의 개수만큼 반복하여 학생 정보출력
                print(student)
        else: #만약 student가 없을경우 
            print("입력된 학생이 없습니다.") #입력된 학생이 없다고 출력
    elif selection == 3: #선택지 3일 경우
        break #반복문을 종료
    else: #1-3의 선택지를 벗어낫을 경우 에러문 출력력
        print("에러 : 1-3 중 하나를 선택하세요.")