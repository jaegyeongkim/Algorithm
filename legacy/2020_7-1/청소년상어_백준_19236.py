import sys
sys.stdin = open('청소년상어.txt')

T = int(input())

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

for t in range(1, T+1):
    fish = [[0]*4 for _ in range(4)]
    for i in range(4):
        arr = list(map(int, input().split()))
        for j in range(4):
            fish[i][j] = [arr[2*j], arr[2*j+1]-1]     #   물고기 번호, 방향

    fish[0][0] = [-1, fish[0][0][1]]
    shark_i, shark_j = 0, 0
    result = 0

    for row in fish:
        print(row)
    print()

    for _ in range(10):
        moved = [0] * 17
        for _ in range(16):
            min_num = 20
            for i in range(4):
                for j in range(4):
                    if fish[i][j][0] > 0 and moved[fish[i][j][0]] == 0:
                        if min_num > fish[i][j][0]:
                            min_num = fish[i][j][0]
                            si, sj = i, j
            if min_num == 20:
                break

            moved[min_num] = 1
            d = fish[si][sj][1]

            while 1:
                ni = si + di[d]
                nj = sj + dj[d]
                if 0 <= ni < 4 and 0 <= nj < 4 and fish[ni][nj][0] != -1:
                    fish[si][sj], fish[ni][nj] = fish[ni][nj], fish[si][sj]
                    break
                else:
                    d += 1
                    if d == 8:
                        d = 0
                    fish[si][sj][1] = d
            # for row in fish:
            #     print(row)
            # print()


        min_num = 20
        d = fish[shark_i][shark_j][1]
        ni = shark_i
        nj = shark_j
        for _ in range(3):
            ni += di[d]
            nj += dj[d]
            if 0 <= ni < 4 and 0 <= nj < 4:
                if min_num > fish[ni][nj][0]:
                    min_num = fish[ni][nj][0]
                    si, sj = ni, nj
        result += fish[si][sj][0]
        fish[si][sj] = [-1, fish[si][sj][1]]
        fish[shark_i][shark_j] = [0, 0]
        for row in fish:
            print(row)
        print()
