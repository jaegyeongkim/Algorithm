import sys
sys.stdin = open('청소년상어.txt')
import copy

def move(board, total, si, sj, ni, nj, fd):
    arr = copy.deepcopy(board)
    arr[si][sj] = [0, 0]
    arr[ni][nj] = [-1, fd]
    selected = [0] * 17
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] > 0:
                selected[arr[i][j][0]] = 1
    while 1:
        if sum(selected) == 0:
            break
        min_fish = 17
        for i in range(4):
            for j in range(4):
                if selected[arr[i][j][0]] == 1:
                    if arr[i][j][0] > 0:
                        if min_fish > arr[i][j][0]:
                            min_fish = arr[i][j][0]
                            fd, fi, fj = arr[i][j][1], i, j

        selected[min_fish] = 0
        while 1:
            ni = fi + di[fd]
            nj = fj + dj[fd]
            if 0 <= ni < 4 and 0 <= nj < 4:
                if arr[ni][nj][0] >= 0:
                    arr[ni][nj], arr[fi][fj] = arr[fi][fj], arr[ni][nj]
                    break
            fd = (fd+1)%9
            if fd == 0:
                fd += 1
            arr[fi][fj][1] = fd

    dfs(arr, total)

def dfs(arr, total):
    global max_total
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == -1:
                si, sj, d = i, j, arr[i][j][1]
    ni = si + di[d]
    nj = sj + dj[d]
    while 1:
        if 0 <= ni < 4 and 0 <= nj < 4:
            if arr[ni][nj][0] > 0:
                fn, fd = arr[ni][nj][0], arr[ni][nj][1]

                move(arr, total+fn, si, sj, ni, nj, fd)
        else:
            if max_total < total:
                max_total = total
            return
        ni += di[d]
        nj += dj[d]




T = int(input())
di = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 0, -1, -1, -1, 0, 1, 1, 1] # 반시계 방향
for t in range(1, T+1):
    arr = [[0] * 4 for _ in range(4)]
    for i in range(4):
        fish = list(map(int, input().split()))
        for j in range(0, len(fish), 2):
            arr[i][j//2] = [fish[j], fish[j+1]]  # 번호, 방향, 이동했나?
    max_total = 0
    total = arr[0][0][0]


    move(arr, total, 0, 0, 0, 0, arr[0][0][1])
    print(max_total)