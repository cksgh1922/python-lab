num_list = []

a = int(input())
b = int(input())    
c = int(input())

sum = str(a*b*c)

for i in range(10):
    count = 0
    for j in range(len(sum)):
        if str(i) == sum[j]:
            count += 1
    print(count)