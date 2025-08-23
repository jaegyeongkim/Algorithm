import sys
sys.stdin = open('스타트 택시.txt')

from collections import deque


T = int(input())

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0] # 상 좌 우 하

def bfs_guest(si, sj, Fuel):
    visited = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append([si, sj, 0, -1, Fuel])
    is_find = 0
    while queue:
        i, j, cnt, d, Fuel = queue.popleft()
        visited[i][j] = 1
        if arr[i][j]%2 == 0 and arr[i][j] != 0:
            if Fuel < 0:
                return -1 -1 -1 -1
            si = i - di[d]
            sj = j - dj[d]
            for d in range(4):
                ni = si + di[d]
                nj = sj + dj[d]
                if arr[ni][nj] > 1:
                    i, j = ni, nj
                    break
            goal = arr[i][j]
            arr[i][j] = 0
            # print(goal, i, j, cnt, Fuel)
            return i, j, goal, Fuel
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                queue.append([ni, nj, cnt+1, d, Fuel-1])

def bfs_destination(si, sj, goal, Fuel):
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append([si, sj, 0, Fuel])
    while queue:
        i, j, cnt, Fuel = queue.popleft()
        print(i, j, Fuel)
        visited[i][j] = 1
        # print(i, j)
        if arr[i][j] == goal+1:
            # if Fuel < 0:
            #     return -1 -1 -1
            arr[i][j] = 0
            Fuel += cnt*2

            # print(goal, i, j, cnt, Fuel)
            return i, j, Fuel
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                queue.append([ni, nj, cnt+1, Fuel-1])


for t in range(1, T+1):
    N, M, Fuel = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    oi, oj = map(int, input().split())
    oi, oj = oi-1, oj-1
    guest = list(list(map(int, input().split())) for _ in range(M))
    cnt = 2
    for si, sj, gi, gj in guest:
        arr[si-1][sj-1], arr[gi-1][gj-1] = cnt, cnt+1
        cnt += 2

    for row in arr:
        print(row)
    for _ in range(M):
        oi, oj, goal, Fuel = bfs_guest(oi, oj, Fuel)
        if Fuel < 0:
            break
        oi, oj, Fuel = bfs_destination(oi, oj, goal, Fuel)
        if Fuel < 0:
            break
        print(Fuel)
