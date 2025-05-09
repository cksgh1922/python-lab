#온도에 따른 운동 추천 프로그램

#입력

degree = float(input("현재 온도(섭씨)를 입력하세요: "))

def recommend():
    if degree < 10:
        print(f"\n현재 온도: {degree}도\n추천 활동: 스키")
    elif 10 <= degree < 20:
        print(f"\n현재 온도: {degree}도\n추천 활동: 자전거 타기")
    elif 20<= degree < 30:
        print(f"\n현재 온도: {degree}도\n추천 활동: 등산")
    else:
        print(f"\n현재 온도: {degree}도\n추천 활동: 수영")

recommend()