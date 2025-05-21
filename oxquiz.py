t = int(input())

for _ in range(t):
    n = input()
    count = 0
    sum = 0
    for char in n:
        if char == "O":
            count += 1
            sum += count
        else:
            count = 0
    print(sum)