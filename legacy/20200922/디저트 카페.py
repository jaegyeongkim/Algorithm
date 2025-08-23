import sys
sys.stdin = open('디저트 카페.txt')

def dfs(i, j, cnt, turn):
    global max_cnt
    desert[arr[i][j]] = 1
    # print(i, j, cnt)
    for d in range(4):
        if turn[d] == 0:
            continue
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N:
            if ni == R and nj == C:
                if max_cnt < cnt:
                    max_cnt = cnt

            if desert[arr[ni][nj]] == 0:
                if d == 0:
                    turn = [1, 1, 0, 0]
                elif d == 1:
                    turn = [0, 1, 1, 0]
                elif d == 2:
                    turn = [0, 0, 1, 1]
                elif d == 3:
                    turn = [0, 0, 0, 1]

                dfs(ni, nj, cnt + 1, turn)

    desert[arr[i][j]] = 0

T = int(input())

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1] # 우하 좌하 좌상 우상

for t in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    max_num = 0
    for i in range(N):
        for j in range(N):
            if max_num < arr[i][j]:
                max_num = arr[i][j]

    max_cnt = -1
    for i in range(N-2):
        for j in range(1, N-1):
            desert = [0] * (max_num+1)

            turn = [1, 1, 0, 0]
            R, C = i, j
            dfs(i, j, 1, turn)
            # print()

    if max_cnt < 4:
        print('#%d' % t, -1)
    else:
        print('#%d'%t, max_cnt)

