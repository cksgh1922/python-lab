import random

while True:
    N = int(input("Enter the size of bingo board ( 3 to 6): "))
    if 3 > N or N > 6:
        print("Size must be between 3 and 6, Please try again.")
    else:
        break

bingo_list = []
while len(bingo_list) != N**2:
    num = random.randint(1,36)
    if num not in bingo_list:
        bingo_list.append(num)
        

print("Initial Bingo Board:")
for i in range(0,len(bingo_list),N):
    print(*bingo_list[i:i+N])



print("Press Enter to generate a random number:")
while True:
    a = input()
    if a == "":
        a = random.randint(1,36)
        print("Random Number :",a)
    for i in range(len(bingo_list)):
        if bingo_list[i] == a:
            bingo_list[i] = "*"
            break
    for i in range(0,len(bingo_list),N):
        print(*bingo_list[i:i+N])
    for i in range(N):
        