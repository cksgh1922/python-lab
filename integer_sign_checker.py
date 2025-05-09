'''
사용자로부터 정수를 입력받아,
해당 정수가 양의 정수인지, 음의 정수인지,
아니면 0인지 판별하는 프로그램 입니다.
'''

# 사용자로부터 정수 입력 받음 ( 입력 값이 정수라고 가정 ) 
inputNumber = int(input("정수 값을 입력하세요: "))

msg = "입력 값은 "

# 입력 받은 값이 양의 정수인 경우 판별
if inputNumber > 0:
	msg = msg + "양수입니다."
elif inputNumber < 0:
	msg = msg +"음수입니다."
else:
	msg = msg + " 0 입니다. "


print(msg)