#구구단 프로그램: 2단부터 9단까지의 구구단을 출력합니다.

for factor in range(2,10): # 2단부터 9단까지의 단 반복문
    for multiplier in range(1,10): # 각 단마다 1부터 9까지 곱할 숫자를 위한 반복문
        print(factor,"X",multiplier,"=",factor*multiplier) # 현재 단과 숫자의 곱을 출력
    print("----------") # 각 단이 끝날 때마다 ----로 구분선 출력