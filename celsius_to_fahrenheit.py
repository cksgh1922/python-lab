#사용자로부터 섭씨 온도를 입력받아 화씨 온도로 변환하는 함수를작성,
#변환된 화씨 온도를 출력하는 프로그램을 작성

#입력받은 섭씨 온도를 화씨 온도로 변환하는 함수 작성
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5) + 32 #  섭씨 값을 화씨 값으로 변환하여 저장

    return fahrenheit #저장된 화씨 값을 리턴

#섭씨 온도를 입력받기
temperature = float(input("섭씨를 입력하세요: "))
#함수 호출 후 출력
print("화씨 온도는 ",convert_celsius_to_fahrenheit(temperature),"입니다.")