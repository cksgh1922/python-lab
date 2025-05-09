n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
    
for i in range(n-1):
    if num_list[i] > num_list[i+1]:
        num_list[i],num_list[i+1] = num_list[i+1],num_list[i]
        
print(*num_list, end="\n")