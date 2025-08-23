import sys
sys.stdin = open('등산로 조성.txt')

def dfs(i, j):
    global max_length
    height = arr[i][j]
    length = 1
    selected = [[0] * N for _ in range(N)]
    stack = [[i, j, height, length, 1]]

    while stack:
        i, j, height, length, possible = stack.pop()
        selected[i][j] = 1

        print(i, j, height, length)

        if max_length < length:
            max_length = length
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if selected[ni][nj] == 0:
                    if arr[ni][nj] < height:
                        selected[i][j] = 1
                        stack.append([ni, nj, arr[ni][nj], length+1, possible])

                    else:
                        if possible:
                            selected[i][j] = 1
                            stack.append([ni, nj, height-1, length+1, 0])


    print()

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] #  상 우 하 좌

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    max_height = 0
    max_length = 0
    for i in range(N):
        for j in range(N):
            if max_height <= arr[i][j]:
                max_height = arr[i][j]
                dfs(i, j)

    # print(max_height_list)
    print(max_length)