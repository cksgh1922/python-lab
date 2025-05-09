N = int(input())
word = []
for i in range(N):
    word.append(str(i+1)+ ". " + input())
    
for i in range(N):
    print(word[i])