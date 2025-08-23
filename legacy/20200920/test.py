import sys

sys.stdin = open('등산로 조성.txt')


def dfs(i, j, height, length, possible):
    global max_length
    if max_length < length:
        max_length = length


    visited[i][j] = 1
    # print(i, j, height, length, possible)
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if height > arr[ni][nj]:
                dfs(ni, nj, arr[ni][nj], length+1, possible)
            else:
                if possible:
                    for k in range(1, K+1):
                        if height > arr[ni][nj] - k:
                            dfs(ni, nj, arr[ni][nj] - k, length+1, 0)
    visited[i][j] = 0

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]  # 상 우 하 좌

for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    max_height = 0
    max_length = 0


    for i in range(N):
        for j in range(N):
            if max_height <= arr[i][j]:
                max_height = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_height:
                length = 1
                visited = [[0] * N for _ in range(N)]
                dfs(i, j, max_height, length, 1)
                # print()

    # print(max_height_list)
    print('#%d'%t, max_length)