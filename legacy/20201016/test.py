import sys
sys.stdin = open('청소년상어.txt')

import copy

def go(arr, arr_dir, x, y, re, sd):
    board = copy.deepcopy(arr)
    board_dir = copy.deepcopy(arr_dir)
    for l in range(1, 17):
        t = False
        for i in range(4):
            for j in range(4):
                if board[i][j] == l:
                    nx = i + dx[board_dir[i][j]]
                    ny = j + dy[board_dir[i][j]]
                    if 0 <= nx <= 3 and 0 <= ny <= 3 and not (nx == x and ny == y):
                        board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                        board_dir[i][j], board_dir[nx][ny] = board_dir[nx][ny], board_dir[i][j]
                        t = True
                        break
                    else:
                        for m in range(1, 7):
                            nx = i + dx[(board_dir[i][j] + m) % 8]
                            ny = j + dy[(board_dir[i][j] + m) % 8]
                            if 0 <= nx <= 3 and 0 <= ny <= 3 and not (nx == x and ny == y):
                                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                                board_dir[i][j] = (board_dir[i][j] + m) % 8
                                board_dir[i][j], board_dir[nx][ny] = board_dir[nx][ny], board_dir[i][j]
                                t = True
                                break
                if t:
                    break
            if t:
                break
    eat(board, board_dir, x, y, re, sd)

def eat(arr1, arr1_dir, x, y, re, sd):
    global ans
    board2 = copy.deepcopy(arr1)
    board2_dir = copy.deepcopy(arr1_dir)
    t = False

    for i in range(1, 5):
        nx = x + i * dx[sd]
        ny = y + i * dy[sd]
        if 0 <= nx <= 3 and 0 <= ny <= 3 and arr1[nx][ny] != 0:
            k = arr1[nx][ny]
            arr1[nx][ny] = -1
            arr1[x][y] = 0
            t = True
            go(arr1, arr1_dir, nx, ny, re + k, arr1_dir[nx][ny])
            arr1[nx][ny] = k
            arr1[x][y] = -1
    if not t:
        if re > ans:
            ans = re
            return
T = int(input())
for t in range(1, T+1):
    a = [list(map(int, input().split())) for _ in range(4)]
    aqua = [[0] * 4 for _ in range(4)]
    direction = [[0] * 4 for _ in range(4)]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    for i in range(4):
        for j in range(4):
            aqua[i][j] = a[i][j * 2]
            direction[i][j] = a[i][j * 2 + 1] - 1

    ans = 0
    shark = [0, 0]
    shark_direction = direction[0][0]
    result = aqua[0][0]
    aqua[0][0] = -1
    go(aqua, direction, 0, 0, result, shark_direction)
    print(ans)
