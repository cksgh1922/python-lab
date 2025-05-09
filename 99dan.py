'''
flag = True
while flag:
    value = int(input("입력 : "))
    
    if value > 0:
        print("입력 값 : ", value)
    else:
        flag = False
        
        '''
        
'''
def menu_print():
    print("------------------")
    print("1. 2단 구구단 출력")
    print("2. 4단 구구단 출력")
    print("3. 프로그램 종료")
    print("----------------")

while True:
    menu_print()
    
    inputValue = int(input("메뉴를 선택해 주세요. : "))
    
    if inputValue == 1:
        for num in range(1, 10):
            print("2 X", num, " = ", 2*num)
    elif inputValue == 2:
        num = 1
        while num <= 9:
            print("4 X ",num," = ",4*num)
            num = num+1
    elif inputValue == 3:
        break
        
    else:
        print("1-3사이 값을 입력해주세요.")
        
'''
'''  
for num in range(1,101):
    if num%7 == 0 and num%11 == 0:
        print(f"7과 11의 최소 공배수는 : {num}")
        break
'''

'''
for value_1 in range(2):
    for value_2 in range(2):
        for value_3 in range(2):
            if value_2 == 1:
                break
            print("value 1 :", value_1,
                  "value 2 :", value_2,
                  "value 3 :", value_3)
'''
'''
for dan in range(2,10):
    
    if dan%3 != 0:
        continue
        
    else:
        for num in range(1,10):
            print(f"{dan} X {num} = {dan*num}",end ="\t")
        
    print()    
    
'''
'''
count = 0
while count < 3: #이쪽으로 이동동
    for value in range(1,3):
        if count == 1:
            continue # 중첩 반복문이있을경우 continue 가 선언된 블록의 반복문으로 이동 
        
        print("count : ", count, ", value : ",value)
    count += 1
'''
'''
print("1")
if 3 > 2:
    pass
    print("2")
print("3")
'''