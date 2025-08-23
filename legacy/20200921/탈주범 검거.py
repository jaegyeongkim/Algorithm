import sys
sys.stdin = open('탈주범 검거.txt')

from collections import deque
def bfs(i, j):
    global total
    cnt = 1
    queue = deque()
    queue.append([i, j, cnt])
    selected[i][j] = 1
    while queue:
        i, j, cnt = queue.popleft()

        if cnt == L:
            continue
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and selected[ni][nj] == 0 and arr[ni][nj] != 0:
                if d == 0:  # 상
                    if pipe[arr[i][j]][0] == 1 and pipe[arr[ni][nj]][2] == 1:
                        queue.append([ni, nj, cnt+1])
                        selected[ni][nj] = 1
                elif d == 1:    # 우
                    if pipe[arr[i][j]][1] == 1 and pipe[arr[ni][nj]][3] == 1:

                        queue.append([ni, nj, cnt + 1])
                        selected[ni][nj] = 1
                elif d == 2:    # 하
                    if pipe[arr[i][j]][2] == 1 and pipe[arr[ni][nj]][0] == 1:

                        queue.append([ni, nj, cnt + 1])
                        selected[ni][nj] = 1
                elif d == 3:    # 좌
                    if pipe[arr[i][j]][3] == 1 and pipe[arr[ni][nj]][1] == 1:
                        queue.append([ni, nj, cnt + 1])
                        selected[ni][nj] = 1

T = int(input())

# 상 우 하 좌
pipe = {
    1: [1, 1, 1, 1],
    2: [1, 0, 1, 0],
    3: [0, 1, 0, 1],
    4: [1, 1, 0, 0],
    5: [0, 1, 1, 0],
    6: [0, 0, 1, 1],
    7: [1, 0, 0, 1],
}

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌

for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    total = 1
    selected = [[0] * M for _ in range(N)]

    bfs(R, C)
    total = 0
    for i in range(N):
        for j in range(M):
            if selected[i][j] == 1:
                total += 1
    print('#%d'%t, total)