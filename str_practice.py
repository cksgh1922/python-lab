'''


def str_to_int(argValue):
    num = 0
    for char in argValue:  # 각 문자마다 반복
        if char in 'ABC':    # A, B, C는 3
            num += 3
        elif char in 'DEF':  # D, E, F는 4
            num += 4
        elif char in 'GHI':  # G, H, I는 5
            num += 5
        elif char in 'JKL':  # J, K, L은 6
            num += 6
        elif char in 'MNO':  # M, N, O는 7
            num += 7
        elif char in 'PQRS': # P, Q, R, S는 8
            num += 8
        elif char in 'TUV':  # T, U, V는 9
            num += 9
        elif char in 'WXYZ': # W, X, Y, Z는 10
            num += 10
    return num


# 사용자 입력 받기
num_str = input()

# 결과 출력
print(str_to_int(num_str))

'''

""