import sys
sys.stdin = open('등산로 조성.txt')

def dfs(i, j, length):
    global max_length

    pass

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(list(map(int, input().split()))for _ in range(N))
    max_height = 0
    for i in range(N):
        for j in range(N):
            if max_height <= arr[i][j]:
                max_height = arr[i][j]
    max_length = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_height:
                for r in range(N):
                    for c in range(N):
                        if r == i and r == j:
                            continue
                        for k in range(K+1):
                            arr[r][c] -= k
                            # dfs(i, j)
                            arr[r][c] += k
                        print(r, c)
                print(i, j)
                print()