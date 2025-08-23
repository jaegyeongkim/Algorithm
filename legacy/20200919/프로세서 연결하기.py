import sys
sys.stdin = open('프로세서 연결하기.txt')


def check_possible(i, j):
    dist_list = []
    cnt_block = 0
    for d in range(4):
        dist_route = []
        dist = 0
        cnt = 0
        while 1:
            cnt += 1
            ni = di[d] * cnt + i
            nj = dj[d] * cnt + j

            if 0 <= nj < N and 0 <= ni < N:
                if arr[ni][nj] == 1:
                    dist = -1
                    break
                dist += 1
                dist_route.append([ni, nj])
            else:
                break
        if dist == -1:
            cnt_block += 1

        dist_list.append([dist, dist_route])
    dist_list.append([0, 0])
    return dist_list


def N_Queen(arr, idx, total, visited, core_cnt):
    global min_total, max_core_cnt

    if idx == the_number_of_core:
        if max_core_cnt < core_cnt:
            max_core_cnt = core_cnt
            min_total = total
            return
        elif max_core_cnt == core_cnt:
            if min_total > total:
                min_total = total
            return
        else:
            return
    for d, route in arr[idx]:
        is_impossible = 0
        path_list = []
        if d == 0 and route == 0:
            N_Queen(arr, idx + 1, total + d, visited, core_cnt)
        elif d > 0:
            for r, c in route:
                if visited[r][c] == 0:
                    visited[r][c] = 1
                    path_list.append([r, c])
                else:
                    for r, c in path_list:
                        visited[r][c] = 0
                    is_impossible = 1
                    break
            if is_impossible:
                continue
            N_Queen(arr, idx + 1, total + d, visited, core_cnt+1)
            for r, c in route:
                visited[r][c] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]  # 상 우 하 좌

    selected = [[0] * N for _ in range(N)]
    min_dist = 0
    Queen_list = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 1:
                result = check_possible(i, j)
                Queen_list.append(result)

    the_number_of_core = len(Queen_list)
    min_total = 100000000
    max_core_cnt = 0
    N_Queen(Queen_list, 0, 0, selected, 0)
    result = min_dist + min_total
    print('#%d' % t, result)