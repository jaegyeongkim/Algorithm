import sys
sys.stdin = open('무선 충전.txt')
from collections import deque

def checktoarr(row, bcnum):
    j, i, length, power = row[0], row[1], row[2], row[3]
    queue = deque()
    queue.append([i, j, 0])
    selected = [[0] * 11 for _ in range(11)]
    selected[i][j] = 1
    if arr[i][j] == 0:
        arr[i][j] = [[bcnum, power]]
    else:
        arr[i][j].append([bcnum, power])
        arr[i][j].sort(key=lambda x: x[1], reverse=True)
    while queue:
        i, j, cnt = queue.popleft()
        for d in range(1, 5):
            ni = i + di[d]
            nj = j + dj[d]
            if 1 <= ni < 11 and 1 <= nj < 11 and selected[ni][nj] == 0:
                if cnt < length:
                    queue.append([ni, nj, cnt+1])
                    selected[ni][nj] = 1
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = [[bcnum, power]]
                    else:
                        arr[ni][nj].append([bcnum, power])
                        arr[ni][nj].sort(key=lambda x:x[1], reverse=True)


def chage(idx):
    ai, aj = A_position[0], A_position[1]
    bi, bj = B_position[0], B_position[1]
    # print(ai, aj, bi, bj)
    if arr[ai][aj] != 0:
        time_table[0][idx] = [arr[ai][aj][0][0], arr[ai][aj][0][1], idx]
    if arr[bi][bj] != 0:
        time_table[1][idx] = [arr[bi][bj][0][0], arr[bi][bj][0][1], idx]


    if time_table[0][idx]!=0 and time_table[1][idx]!=0:
        if time_table[0][idx][0] == time_table[1][idx][0]:
            # A가 2 이상이고 B는 1일때
            if len(arr[ai][aj]) > 1 and len(arr[bi][bj]) == 1:
                time_table[0][idx] = [arr[ai][aj][1][0], arr[ai][aj][1][1], idx]
            # B가 2 이상이면 A는 1일때
            elif len(arr[bi][bj]) > 1 and len(arr[ai][aj]) == 1:
                time_table[1][idx] = [arr[bi][bj][1][0], arr[bi][bj][1][1], idx]
            # A, B 둘 다가 2이상일때
            elif len(arr[ai][aj]) > 1 and len(arr[bi][bj]) > 1:
                if arr[ai][aj][1][1] > arr[bi][bj][1][1]:
                    time_table[0][idx] = [arr[ai][aj][1][0], arr[ai][aj][1][1], idx]
                else:
                    time_table[1][idx] = [arr[bi][bj][1][0], arr[bi][bj][1][1], idx]
            # 둘 다 1
            elif len(arr[ai][aj]) == 1 and len(arr[bi][bj]) == 1:
                time_table[0][idx][1] = time_table[0][idx][1]//2
                time_table[1][idx][1] = time_table[1][idx][1]//2
    # for row in arr:
    #     print(row)
    # for row in time_table:
    #     print(row)
    # print()
T = int(input())

di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1] # 상 우 하 좌

for t in range(1, T+1):
    M, A = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))
    BC_data = list(list(map(int, input().split())) for _ in range(A))
    arr = [[0]*11 for _ in range(11)]
    time_table = [[0]*(M+1) for _ in range(2)]  # 이동 충전


    A_position = [1, 1, "A"]
    B_position = [10, 10, "B"]
    # arr에 표시하기
    bcnum = 1
    for row in BC_data:
        checktoarr(row, bcnum)
        bcnum += 1
    # for row in arr:
    #     print(row)
    chage(0)
    # for row in arr:
    #     print(row)
    for d in range(M):
        da = A_arr[d]
        db = B_arr[d]
        A_position[0] += di[da]
        A_position[1] += dj[da]
        B_position[0] += di[db]
        B_position[1] += dj[db]

        chage(d+1)

    total = 0
    for row in time_table:
        for column in row:
            if column != 0:
                total += column[1]
    print('#%d'%t, total)
