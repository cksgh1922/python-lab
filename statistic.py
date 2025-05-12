import random
import math

#리스트 elements 개수 입력받기
list_num = int(input("리스트 개수를 입력하세요 (5~20): "))
if list_num < 5 or list_num > 20:
    print("오류 : 리스트 개수는 5 이상 20 이하여야 합니다.")
else:
        
    
    #리스트 생성
    data_list = []

    #입력받은 list_num 만큼 반복하여 난수를 생성하고, 이를 list에 추가
    data_list = [random.randint(1,100) for _ in range(list_num)]

    #리스트 총합을 계산하는 반복문
    total = 0
    for val in data_list:
        total += val

    #리스트 평균을 계산하여 avg 변수에 저장
    avg = total / list_num


    #편차를 계산하는 반복문
    deviation = []
    for val in data_list:
        deviation.append(val-avg)

    #모든 편차제곱의 합을 계산하는 반복문
    variance = 0
    for val in deviation:
        variance += val**2

    #모든 편차 제곱의 합을 데이터 개수로 나누어 variance에 저장
    variance /= list_num

    #표준편차값을 root에 저장
    root = math.sqrt(variance)


    #출력문
    print(f"""
    생성된 리스트 : {data_list}
    평균 : {avg:.2f}
    편차 : {[round(val,2) for val in deviation]}
    분산 : {variance:.2f}
    표준편차 : {root:.2f}""")