#사용자로부터 거리를 입력받아 빛이 해당 거리를
#여행하는데 걸리는 시간을 계산하는 프로그램 작성

#사용자로부터 거리를 킬로미터 단위로 입력받는다.
distance = float(input("여행할 거리를 킬로미터(km) 단위로 입력하세요 : "))

#빛의 속도 = 초당 299,792킬로미터이므로 입력받은 값을 속도로 나눈다.
time = distance/299792

#빛의 속도로 얼마나 걸리는지 출력한다.
print("빛이 ",distance,"킬로미터를 여행하는 데 걸리는 시간은 ",time,"초 입니다.")