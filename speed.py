#평균 속도를 계산하는 프로그램

#입력
departTime_hour = int(input("출발 시 (시간)을 입력하세요: "))
departTime_minutes = int(input("출발 시 (분)을 입력하세요: "))
arriveTime_hour = int(input("도착 시 (시간)을 입력하세요: "))
arriveTime_minutes = int(input("도착 시 (분)을 입력하세요: "))
distance = float(input("이동 거리(km)를 입력하세요: "))


#평균 속도를 계산하는 함수
def kilo_per_hour():
    a = distance/took_hour
    print(f"평균 속도: {a:.2f}km/h")
    return a
    
#시간 변환 함수
def time_change(a,b):
    changed_time = ((a*60) + b)/60

    return changed_time
    
#시간 계산 함수
def time_calculate():
    a =  (changed_arrive_time - changed_depart_time)
    if a < 0:
        a *= -1
        return a
    else:
        return a
        
#시속에 따라 출력하는 함수
def fast_or_slow():
    if speed < 60:
        print("속도 상태: 느림")
    elif 60<= speed < 90:
        print("속도 상태: 보통")
    else:
        print("속도 상태: 빠름")

#이동 거리를 출력
print(f"이동 거리: {distance}km")

#출발 시간을 출력
print(f"출발 시간: {departTime_hour}시 {departTime_minutes}분")

#도착 시간을 출력
print(f"도착 시간: {arriveTime_hour}시 {arriveTime_minutes}분")

#시간 변환 함수를 호출해 출발 시간 변환
changed_depart_time = time_change(departTime_hour,departTime_minutes)

#시간 변환 함수를 호출해 도착 시간 변환
changed_arrive_time = time_change(arriveTime_hour,arriveTime_minutes)

#출발, 도착 시간 계산
took_hour = time_calculate()

#평균 속도 계산 및 출력 함수
speed = kilo_per_hour()

#속도 상태를 판별하여 출력하는 함수 호출
fast_or_slow()