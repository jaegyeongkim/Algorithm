import sys
sys.stdin = open('음식 배달.txt')
import copy
from collections import deque
def check(market):
    global min_total
    new_arr = copy.deepcopy(arr)

    for i, j, cost in market:
        new_arr[i][j] = 0

    visited = [[0]*(N+1) for _ in range(N+1)]
    total_dist = 0

    for i in range(N+1):
        for j in range(N+1):
            if new_arr[i][j] == 1:
                if visited[i][j] == 0:
                    selected = [[0]*(N+1) for _ in range(N+1)]
                    visited[i][j] = 1
                    selected[i][j] = 1
                    queue = deque()
                    queue.append([i, j, 0])
                    while queue:
                        r, c, dist = queue.popleft()
                        if new_arr[r][c] > 1:
                            if visited[r][c] == 0:
                                visited[r][c] = 1
                                total_dist += new_arr[r][c]

                            break
                        for d in range(4):
                            nr = r + di[d]
                            nc = c + dj[d]
                            if 1 <= nr < N+1 and 1 <= nc < N+1 and selected[nr][nc] == 0:
                                queue.append([nr, nc, dist+1])
                                selected[nr][nc] = 1
                    total_dist += dist
    if min_total > total_dist:
        min_total = total_dist
def powerset(idx):
    if idx == len(markets):
        if sum(selected) > 0:
            market = []
            for i in range(len(markets)):
                if selected[i] == 0:
                    market.append(markets[i])
            check(market)
        return
    selected[idx] = 1
    powerset(idx+1)
    selected[idx] = 0
    powerset(idx+1)

T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for t in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+1)] + list([0] + list(map(int, input().split())) for _ in range(N))
    markets = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] > 1:
                markets.append([i, j, arr[i][j]])
    min_total = 10000000000
    selected = [0] * len(markets)
    powerset(0)
    print('#%d'%t, min_total)