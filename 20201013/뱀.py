import sys
sys.stdin = open('뱀.txt')

def dfs(i, j):
    stack = [[i, j, 1]] # i, j, 방향
    time = 0
    arr[i][j] = 1
    visited = [[i, j]]
    while stack:

        time += 1
        i, j, d = stack.pop()
        ni = i + di[d]
        nj = j + dj[d]

        if 1 <= ni < N+1 and 1 <= nj < N+1:
            if arr[ni][nj] == 1:
                return time

            elif arr[ni][nj] == 2:
                arr[ni][nj] = 1
                visited.append([ni, nj])
            elif arr[ni][nj] == 0:
                arr[ni][nj] = 1
                arr[visited[0][0]][visited[0][1]] = 0
                visited.pop(0)
                visited.append([ni, nj])

            if direction[time] != 0:
                if direction[time] == "L":
                    d = (d+3)%4
                elif direction[time] == "D":
                    d = (d+1)%4
            stack.append([ni,nj,d])
        else:
            return time
        # print(time)
        # print(visited)
        # for row in arr:
        #     print(row)
        # print()


T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for t in range(1, T+1):
    N = int(input())
    K = int(input())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for k in range(K):
        i, j = map(int, input().split())
        arr[i][j] = 2
    L = int(input())
    direction = [0] * 10010
    max_time = 0
    for i in range(L):
        time, d = map(str, input().split())
        time = int(time)

        direction[time] = d


    print(dfs(1, 1))

