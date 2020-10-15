import sys
from itertools import combinations
sys.stdin = open('사다리 조작.txt')
def check_short(comb):
    for i in range(len(comb)):
        arr[comb[i][0]][comb[i][1]] = comb[i][1]+1
        arr[comb[i][0]][comb[i][1]+1] = comb[i][1]
    result = movement()
    for i in range(len(comb)):
        arr[comb[i][0]][comb[i][1]] = 0
        arr[comb[i][0]][comb[i][1]+1] = 0
    return result
def movement():
    for c in range(1, N+1):
        sc = c
        r = 0
        while 1:
            r += 1
            if r == H+1:
                r -= 1
                if sc != c:
                    return 0
                break
            if arr[r][c] == 0:
                continue
            else:
                c = arr[r][c]
    return 1

T = int(input())
for t in range(1, T+1):
    N, M, H = map(int, input().split())
    info = list(list(map(int, input().split())) for _ in range(M))
    arr = [[0] * (N + 1) for _ in range(H + 1)]
    for i in range(len(info)):
        arr[info[i][0]][info[i][1]] = info[i][1] + 1
        arr[info[i][0]][info[i][1] + 1] = info[i][1]
    if movement() == 1:
        print(0)
    else:
        min_length = 4
        check = []
        for i in range(1, H + 1):
            for j in range(1, N + 1):
                if arr[i][j] == 0:
                    if j + 1 < N + 1:
                        if arr[i][j + 1] == 0:
                            check.append([i, j])
        for i in range(1, 4):
            comb = list(combinations(check,i))
            for j in range(len(comb)):
                result = check_short(comb[j])
                if result == 1:
                    if min_length > len(comb[j]):
                        min_length = len(comb[j])
        if min_length == 4:
            print(-1)
        else:
            print(min_length)