num_list = []

def find_high_num():
    max_num = num_list[0][0]
    for i in range(9):
        for j in range(9):
            if num_list[i][j] > max_num:
                max_num = num_list[i][j]
    
    #이 아래부터 함수 끝나는 곳 까지 공부 (처음배움움)
    index_location = None
    for i , row in enumerate(num_list):
        if max_num in row:
            index_location = (i+1,row.index(max_num)+1)
            break
    return max_num, index_location    


for i in range(9):
    input_list = list(map(int,input().split()))
    num_list.append(input_list)
    input_list = []

max_num , index_locaton = find_high_num()

print(max_num)
print(*index_locaton)