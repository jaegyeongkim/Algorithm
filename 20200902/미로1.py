import sys
sys.stdin = open("미로1.txt")

T = 10

def dfs(si, sj):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    visited = [[0] * L for _ in range(L)]
    stack = [[si, sj]]
    while stack:
        i, j = stack.pop()
        visited[i][j] = 1
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < L and 0 <= nj < L and visited[ni][nj] == 0:
                if maze[ni][nj] == 0:
                    stack.append([ni, nj])
                elif maze[ni][nj] == 3:
                    return 1
    return 0



for t in range(1, T+1):
    N = int(input())
    L = 16
    maze = list(list(map(int, input())) for _ in range(L))

    r, c = 0, 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                r, c = i, j
                break
        if r !=0 and c != 0:
            break

    print('#%d'%t, dfs(r, c))

