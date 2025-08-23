import sys
sys.stdin = open('줄기세포배양.txt')
from collections import deque
def bfs():
    cnt = 1
    while cnt < K:
        for i in range(length//2-N*2-cnt, length//2+N*2+cnt, 1):
            for j in range(length//2-M*2-cnt, length//2+M*2+cnt, 1):
                if new_arr[i][j] != 0:
                    life, left, time, state = new_arr[i][j][0], new_arr[i][j][1], new_arr[i][j][2], new_arr[i][j][3]
                    left -= 1
                    print(i-190, j-190, life, left, time)
                    if left > 0:
                        new_arr[i][j] = [life, left, cnt, 0]
                    elif left == 0:
                        new_arr[i][j] = [life, left, cnt, -1]
                        for d in range(4):
                            ni = i + di[d]
                            nj = j + dj[d]
                            if 0 <= ni < length and 0 <= nj < length:
                                if selected[ni][nj] == 0:
                                if new_arr[ni][nj] == 0:
                                    new_arr[ni][nj] = [life, life+1, cnt, 0]

                                else:
                                    if cnt == new_arr[ni][nj][2]:

                                        if life > new_arr[ni][nj][0]:
                                            new_arr[ni][nj] = [life, life+1, cnt, 0]
                                selected[ni][nj] = 1
        print(cnt)
        for i in range(190, 210):
            for j in range(190, 210):
                print(new_arr[i][j], end=' ')
            print()
        print()
        cnt += 1

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    length = 400
    new_arr = [[0] * length for _ in range(length)]
    queue = deque()
    selected = [[0] * length for _ in range(length)]

    for i in range(N):
        for j in range(M):
            left, time = 0, 0
            if arr[i][j] > 0:
                life = arr[i][j]
                new_arr[i+length//2][j+length//2] = [life, life+1, 0, 0]
                selected[i][j] = 1


    bfs()