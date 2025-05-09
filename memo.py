
'''
A = input()

B = 'aeiou'

for char in A:
    if char in B:
        print("true")
    else:
        print("false")
        
'''

'''
bar = 3
foo = 2
sum = bar+foo
sub = bar-foo
mul = bar*foo
div = bar/foo

print(f"sum: {sum}\nsub: {sub}\nmul: {mul}\ndiv: {div}")
'''
'''
result1 = 3//2
result2 = 3/2
print(result1,result2)

for divisor in range(6):
    print(divisor%3)
    
    
count = 1

for dan in range(2, 10):
    for num in range(1,10):
        print(f"{dan} X {num} = {dan*num}")
    if count % 3 == 0:
        print("=================")
    count+=1
'''
'''
result = 2**3

print(result)

for value in range (11):
    print(2**value)
    '''
'''   
def returnNum(argNum):
    print(f"argNum: {argNum}\treturnNum() is invoked")
    return argNum
returnNum(1)


if True and returnNum(2) == 2:
    print("True")
if False and returnNum(3) == 2:
    print("True")
if True or returnNum(4) == 4:
    print("True")
if False or returnNum(5) == 4:
    print("True")
    
    '''
'''    
bar = 1
foo = 1

kin = bar

if bar is not kin:
    print("true")
else:
    print("false")
    '''
    
"""
print("1")
if False:
    print("T 1-1")
    print("T 1-2")
print("3")
"""

'''
corp = ["SK","SAMSUNG","NAVER","LG","KAKAO","HYUNDAI"]
a = input()

if a == corp[0]:
    print("에스케이")
elif a == corp[1]:
    print("삼성")
elif a == corp[2]:
    print("네이버")
elif a == corp[3]:
    print("엘지")
elif a == corp[4]:
    print("카카오")
elif a == corp[5]:
    print("현대")
else:
    print("그 외")
    '''
"""
a = int(input())
for index in range(1,a):
    value = str(index)
    flag = False
    msg = ""
    for index_char in value:
        if index_char == "3" or index_char == "6" or index_char == "9":
            msg += "박수 "
            flag = True
    if flag:
        print(msg)
    else:
        print(index)
"""
'''
# def 함수이름 (매개변수, parameter)
def add(x,y): # 인자값(argument) : 2,3  -> x, y = 매개변수 (paramater) 
    result = x+y
    return result
# 함수이름 (인자값,argument)
result1 = add(2,3)
result2 = add(5,6)

print(f"result1:{result1},result2:{result2}")
'''

# shopping_list = []
# shopping_list += "milk",'bread','eggs','apple'

# print("now",shopping_list)
# shopping_list.insert(0,'toilet paper')
# shopping_list.insert(1,'orange juice')
# shopping_list.extend(['chicken','rice'])
# print("last",shopping_list)

# def even_odd(num):
#     if num % 2 == 0:
#         print("짝수입니다")
#     else:
#         print("홀수입니다")
        
# def positive_negative(num):
#     if num > 0:
#         print("양수입니다.")
#     elif num < 0:
#         print("음수입니다.")
#     else:
#         print("0입니다.")

# size_of_rect = int(input("가로 or 세로 길이 : "))

# print(f"정사각형의 넓이는 {size_of_rect**2}입니다. ")

bar = "hello"

del bar
print(bar)