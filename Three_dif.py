#세 수의 비교, 유사성 차이점 찾기
# 모든수가 같은지, 두수만같은지 (두수 모두 출력), 다 다른지 확인
def num_dif(num1,num2,num3):
    if num1 == num2 == num3:
        return "모든 수가 같습니다."
    
    if num1 == num2:
        return f"두 수가 같습니다. ({num1}와{num2})"
    elif num2 == num3:
        return f"두 수가 같습니다. ({num2}와{num3})"
    elif num1 == num3:
        return f"두 수가 같습니다. ({num1}와{num3})"
    else:
        big_num = max(num1,num2,num3)
        return f"모든 수가 다릅니다. 가장 큰 수는 {big_num}입니다."
        

#세 수 입력받기
num1 = int(input("첫 번째 수 입력: "))
num2 = int(input("두 번째 수 입력: "))
num3 = int(input("세 번째 수 입력: "))


#함수 호출 및 출력
print(num_dif(num1,num2,num3))
