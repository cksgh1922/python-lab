#수를 10개 입력 받는다
a = []
for i in range(10):
    a.append(int(input()))
    a[i] = a[i]%42
unique_count = len(set(a))

# set()함수 다시 공부해보기

