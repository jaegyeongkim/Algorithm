import sys
sys.stdin = open('구슬 탈출2.txt')
from collections import deque

def move(i, j, d):
    count = 0
    while arr[i+di[d]][j+dj[d]] != '#' and arr[i][j] != 'O':
        i += di[d]
        j += dj[d]
        count += 1
    return i, j, count

def dfs(ri, rj, bi, bj):
    visited[ri][rj][bi][bj] = 1
    queue = deque()
    queue.append([ri, rj, bi, bj, 1])
    while queue:
        ri, rj, bi, bj, cnt = queue.popleft()
        if cnt > 10:
            break
        for d in range(4):
            nri, nrj, r_cnt = move(ri, rj, d)
            nbi, nbj, b_cnt = move(bi, bj, d)
            if arr[nbi][nbj] == 'O':
                continue
            if arr[nri][nrj] == 'O':
                print(cnt)
                return
            if nri == nbi and nrj == nbj:
                if r_cnt > b_cnt:
                    nri -= di[d]
                    nrj -= dj[d]
                else:
                    nbi -= di[d]
                    nbj -= dj[d]

            if visited[nri][nrj][nbi][nbj] == 0:
                visited[nri][nrj][nbi][nbj] = 1
                queue.append([nri, nrj, nbi, nbj, cnt+1])
    print(-1)

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))
    visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                ri, rj = i, j
            elif arr[i][j] == 'B':
                bi, bj = i, j
            elif arr[i][j] == 'O':
                oi, oj = i, j
    dfs(ri, rj, bi, bj)