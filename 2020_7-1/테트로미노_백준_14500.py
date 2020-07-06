import sys
sys.stdin = open('테트로미노.txt')

T = int(input())

def a_1(i, j):
    if j+3 >= M:
        return 0
    result = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
    return result

def a_2(i ,j):
    if i+3 >= N:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
    return result

def b_1(i, j):
    if i+1 >= N or j+1 >= M:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
    return result

def c_1(i, j):
    if i-1 < 0 or j+2 >= M:
        return 0
    result = arr[i][j] + arr[i-1][j] + arr[i-1][j+1] + arr[i-1][j+2]
    return result

def c_2(i, j):
    if i+2 >= N or j+1 >= M:
        return 0
    result = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
    return result

def c_3(i, j):
    if i+1 >= N or j-2 < 0:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j-2]
    return result

def c_4(i, j):
    if i+2 >= N or j+1 >= M:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
    return result

def c_5(i, j):
    if i+1 >= N or j+2 >= M:
        return 0
    result = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
    return result

def c_6(i, j):
    if i+2 >= N or j-1 < 0:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j-1]
    return result

def c_7(i, j):
    if i+1 >= N or j+2 >= M:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
    return result

def c_8(i, j):
    if i+2 >= N or j-1 < 0:
        return 0
    result = arr[i][j] + arr[i][j-1] + arr[i+1][j-1] + arr[i+2][j-1]
    return result

def d_1(i, j):
    if i+2 >= N or j+1 >= M:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
    return result

def d_2(i, j):
    if i-1 < 0 or j+2 >= M:
        return 0
    result = arr[i][j] + arr[i][j+1] + arr[i-1][j+1] + arr[i-1][j+2]
    return result

def d_3(i, j):
    if i+2 >= N or j-1 < 0:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+2][j-1]
    return result

def d_4(i, j):
    if i+1 >= N or j+2 >= M:
        return 0
    result = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
    return result

def g_1(i, j):
    if i-1 < 0 or j+2 >= M:
        return 0
    result = arr[i][j] + arr[i][j+1] + arr[i-1][j+1] + arr[i][j+2]
    return result

def g_2(i, j):
    if i+2 >= N or j-1 < 0:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i][j-1]
    return result

def g_3(i, j):
    if i+1 >= N or j+2 >= M:
        return 0
    result = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
    return result

def g_4(i, j):
    if i+2 >= N or j+1 >= M:
        return 0
    result = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1]
    return result

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))


    result = 0
    for i in range(N):
        for j in range(M):
            result = max(a_1(i, j), a_2(i, j), b_1(i, j), c_1(i, j), c_2(i, j), c_3(i, j), c_4(i, j), c_5(i, j), c_6(i, j), c_7(i, j), c_8(i, j), d_1(i, j), d_2(i, j), d_3(i, j), d_4(i, j), g_1(i, j), g_2(i, j), g_3(i, j), g_4(i, j), result)
    print(result)