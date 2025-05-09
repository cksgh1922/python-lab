N,M = map(int,input().split())
ppl = N*M

guess = list(map(int,input().split()))

answear = []
for i in range(len(guess)):
    answear.append(guess[i] - ppl)

print(*answear)