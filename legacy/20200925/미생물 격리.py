import sys
sys.stdin = open('미생물 격리.txt')

def move(i, j, bd_list):
    b, d = bd_list[0], bd_list[1]
    ni = i + di[d]
    nj = j + dj[d]

    if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
        b = b // 2
        if d == 1:
            d = 2
        elif d == 2:
            d = 1
        elif d == 3:
            d = 4
        elif d == 4:
            d = 3

    arr[i][j] = 0
    stack = [ni, nj, b, d]

    return stack
T = int(input())

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1] # 상 하 좌 우

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    bacteria = list(list(map(int, input().split())) for _ in range(K))
    arr = [[0] * N for _ in range(N)]

    for r, c, b, d in bacteria:
        arr[r][c] = [b, d]


    for m in range(M):
        bacteria_cnt = [[0] * N for _ in range(N)]
        movemoent_list = []
        for i in range(N):
            for j in range(N):
                if arr[i][j] != 0:
                    movemoent_list.append(move(i, j, arr[i][j]))

        for ni, nj, nb, nd in movemoent_list:
            if arr[ni][nj]:
                arr[ni][nj][0] += nb
                if bacteria_cnt[ni][nj][0] < nb:
                    bacteria_cnt[ni][nj][0] = nb
                    arr[ni][nj][1] = nd
            else:
                arr[ni][nj] = [nb, nd]
                bacteria_cnt[ni][nj] = [nb, nd]
        # for row in arr:
        #     print(row)
        # print()
    total = 0
    for i in range(len(movemoent_list)):
        total += movemoent_list[i][2]
    print('#%d'%t, total)
