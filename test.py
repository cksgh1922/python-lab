'''
numbers = [4,2,3,1]
print("원래 순서: ",numbers)

numbers.append(5)
print("추가 후", numbers)

numbers.remove(2)
print("제거 후",numbers)

mixed_list = [1,"apple",3.14,[2,4,6],True]

print("혼합 데이터 타입 리스트 : ", mixed_list)

squares = [x**2 for x in range(12)]
print("리스트 컴프리핸션: ",squares)
'''
'''
def change(x,y):
    global basket
    basket[x-1:y] = basket[x-1:y][::-1] 
    
    
N, M  = map(int,input().split())
basket = []
for i in range(N):
    basket.append(i+1)
for i in range(M):
    num1 , num2 = map(int,input().split())
    change(num1,num2)

for i in range(N):
    print(basket[i],end=" ")
    
'''
'''
#다시 해보기 씨발
def jujak():
    total = 0
    for i in range(num):
        total += (subject_score[i]/high_score)*100
    g = total/num
    return g

num = int(input())

subject_score = list(map(int,input().split()))


high_score = max(subject_score)

print(jujak())
'''
# 이거도 다시 해보기

# def put_ball():
#     global basket
#     for i in range(from_basket -1, to_basket):
#         basket[i] = number
    
    
    
# N, M  = map(int,input().split())
# basket = [0]*N

# for i in range(M):
#     from_basket , to_basket , number = map(int,input().split())
#     put_ball()

# print(*basket)
# 다시 좀 하자.....0


n = 5
inputValueList = []
for index in range(n):
    indexValue = input(str(index+1) + "번째입력값")
    inputValueList.append(int(indexValue))

for iCount in range(n-1):
    for jCount in range(n - iCount -1):
        if inputValueList[jCount] < inputValueList[jCount + 1]:
            temp = inputValueList[jCount+1]
            inputValueList[jCount + 1] = inputValueList[jCount]
            inputValueList[jCount] = temp

print(inputValueList)
    