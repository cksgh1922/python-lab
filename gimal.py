#학번과 학번에 해당하는 value값을 저장할 딕셔너리 생성
students = {}
#학생 정보 입력받기
def input_student(students):
    std_num = input("학번 입력: ")
    if std_num in students:
        print("이미 등록된 학번입니다.")
    else:
        students[std_num] = {}
        students[std_num]['name'] = input("이름 입력: ")
        students[std_num]['k-score'] = int(input("국어 성적 입력: "))
        students[std_num]['m-score'] = int(input("수학 성적 입력: "))
        students[std_num]['e-score'] = int(input("영어 성적 입력: "))
        students[std_num]['total'] = students[std_num]['k-score']+students[std_num]['m-score']+students[std_num]['e-score']
        students[std_num]['avg'] = students[std_num]['total'] / 3
        print("성적이 저장되었습니다.")

#전체 학생 정보 출력
def print_all_students(students):
    if not students:
        print("저장된 학생 정보가 없습니다.")
    else:
        print("""
[ 전체 학생 성적 ]
학번\t이름\t국어\t영어\t수학\t합계\t평균""")
        
    for key, value in students.items():
        print(f"""{key}\t{value['name']}\t{value['k-score']}\t{value['m-score']}\t{value['e-score']}\t{value['total']}\t{value['avg']}""")
        
#학생 정보 찾아서 하나만 출력
def search_student(students):
    std_num = input("조회할 학번 입력: ")
    
    msg = f"""
[ 학생 정보 ]
학번: {std_num}
이름: {students[std_num]['name']}
국어: {students[std_num]['k-score']}
영어: {students[std_num]['e-score']}
수학: {students[std_num]['m-score']}
합계: {students[std_num]['total']}
평균: {students[std_num]['avg']}"""


    if std_num in students:
        print(msg)
    else:
        print("해당 학번의 학생 정보가 없습니다.")

#학생 정보 삭제
def delete_student(students):
    std_num = input("삭제할 학번 입력: ")
    if std_num in students:
        del students[std_num]
        print("학생 정보가 삭제되었습니다.")
    else:
        print("해당 학번의 학생 정보가 없습니다.")

#main함수
while True:
    #출력문
    n = int(input("""
==== 학생 성적 관리 프로그램 ====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료
메뉴 선택 (1~5): """))
    #C
    if n == 1:
        input_student(students)
    #R
    elif n == 2:
        print_all_students(students)
    #R
    elif n == 3:
        search_student(students)
    #D
    elif n == 4:
        delete_student(students)
    #Break
    elif n == 5:
        print("프로그램을 종료합니다.")
        break
    #예외처리
    else:
        print("잘못된 입력입니다.")

#key값 접근 방식 공부하기.