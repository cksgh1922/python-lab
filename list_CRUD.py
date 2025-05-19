#5번 카운트할 n 변수 생성
n = 0
#정수를 저장할 리스트 생성
num_list = []
#반복문 시작
while n < 5:
#메뉴 출력
    option = int(input("""
작업을 선택하세요 :
1: 추가 (Create)
2: 조회 (Read)
3: 수정 (Update)
4: 삭제 (Delete)
5: 종료 (Exit)
입력: """))
    #추가일 경우 리스트에 입력받은 값 추가 후 카운트 증가
    if option == 1:
        num_list.append(int(input("추가할 값을 입력하세요: ")))
        print("추가 완료.")
        n+=1
    #조회일경우 리스트 읽은 후 카운트 증가
    elif option == 2:
        print("[현재 리스트 내용]")
        for i in range(len(num_list)):
            print(f"{i}:{num_list[i]}")
        n+=1
    #수정일 경우 수정할 인덱스 입력받고 값 수정 후 카운트 증가
    elif option == 3:
        index_num = int(input("수정할 인덱스를 입력하세요: "))
        #만약 리스트 길이보다 입력받은 인덱스 값이 클 경우 오류 출력
        if index_num >= len(num_list):
            print("유효하지 않은 인덱스입니다.")
        else:
            num_list[index_num] = int(input("새로운 값을 입력하세요: "))
            print("수정 완료.")
        n+=1
    #삭제일 경우 삭제할 인덱스를 입력받고 삭제 후 카운트 증가
    elif option == 4:
        index_num = int(input("삭제할 인덱스를 입력하세요: "))
        #만약 리스트 길이보다 입력받은 인덱스 값이 클 경우 오류 출력
        if index_num >= len(num_list):
            print("유효하지 않은 인덱스입니다.")
        else:
            del num_list[index_num]
        n+=1
    #입력이 종료일 경우 프로그램 종료 출력 후 반복문 종료
    elif option == 5:
        print("프로그램을 종료합니다.")
        break
    #유효한 입력이 아닐 경우 오류문 출력
    else:
        print("올바른 번호를 입력하세요.")
#프로그램 종료문 출력
if option != 5:
    print("모든 입력 기회를 다 사용했습니다. 프로그램을 종료합니다.")