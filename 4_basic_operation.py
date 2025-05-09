#두 자연수 A,B를 입력받아, 두 수의 합,차,곱,몫을을
#출력하는 프로그램을 작성

#두 수를 입력받는다.
num1 = int(input("첫 번째 숫자를 입력하세요:"))
num2 = int(input("두 번째 숫자를 입력하세요:"))

#두개의 값을 입력받아 더한 값을 출력하는 함수를 작성
def plus(argValueA,argValueB):
    #입력 받은 두 개의 수를 더한 후 실수형으로 전환
    result = float((argValueA + argValueB))
    #출력 메세지 작성 후 출력력
    print("합 :",result)
    
#두개의 값을 입력받아 뺀 값을 출력하는 함수를 작성
def minus(argValueA,argValueB):
    #입력 받은 두 개의 수를 뺀 후 실수형으로 전환
    result= float((argValueA-argValueB))
    #출력 메세지 작성 후 출력
    print("차 :",result)

#두개의 값을 입력받아 뺀 값을 출력하는 함수를 작성
def multiply(argValueA,argValueB):
    #입력 받은 두 개의 수를 곱한한 후 실수형으로 전환
    result= float((argValueA*argValueB))
    #출력 메세지 작성 후 출력
    print("곱 :",result)
    
#두개의 값을 입력받아 나눈 값을 출력하는 함수를 작성
def divide(argValueA,argValueB):
    #입력 받은 두 개의 수를 나눈 후 실수형으로 전환
    result= float((argValueA/argValueB))
    #출력 메세지 작성 후 출력
    print("나눗셈 :",result)

#합,차,곱,나눔을 해서 출력하는 함수 실행행
plus(num1,num2)
minus(num1,num2)
multiply(num1,num2)
divide(num1,num2)

'''
num1 = int(input())
num2 = int(input())

print("합 :",float(num1+num2))
print("차 :",float(num1-num2))
print("곱 :",float(num1*num2))
print("나눗셈 :",float(num1/num2))
'''