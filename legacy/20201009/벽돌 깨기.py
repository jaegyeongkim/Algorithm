import sys
sys.stdin = open('벽돌 깨기.txt')

def crash(copy):
    new_arr = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            new_arr[i][j] = arr[i][j]
    # print(copy)
    for j in copy:
        for i in range(H):
            crash_list = []
            if new_arr[i][j] == 1:
                new_arr[i][j] = 0
                break
            elif new_arr[i][j] > 1:
                # 여기서 부터는 dfs
                stack = []
                stack.append([i, j])
                crash_list.append([i, j])
                selected = [[0] * W for _ in range(H)]
                selected[i][j] = 1
                while stack:
                    i, j = stack.pop()

                    for d in range(4):
                        for n in range(1, new_arr[i][j]):
                            ni = i + di[d]*n
                            nj = j + dj[d]*n
                            if 0 <= ni < H and 0 <= nj < W and selected[ni][nj] == 0:
                                if new_arr[ni][nj] > 0:
                                    if new_arr[ni][nj] > 1:
                                        stack.append([ni, nj])
                                    selected[ni][nj] = 1
                                    crash_list.append([ni, nj])
                # print(crash_list)
                for i, j in crash_list:
                    new_arr[i][j] = 0
                break

        crash_list.sort(key=lambda x:x[0])

        # print(crash_list)
        for i, j in crash_list:
            for bi in range(i):
                new_arr[i-bi][j] = new_arr[i-bi-1][j]
                new_arr[i-bi-1][j] = 0



    # for row in new_arr:
    #     print(row)
    # print()
    cnt = 0
    for i in range(H):
        for j in range(W):
            if new_arr[i][j] > 0:
                cnt += 1
    return cnt


def permutation(idx):
    global max_cnt
    if max_cnt == 0:
        return
    if idx == N:
        # print(copy)
        cnt = crash(copy)
        if max_cnt > cnt:
            max_cnt = cnt

        return
    else:
        for i in range(W):
            copy[idx] = range_list[i]
            permutation(idx+1)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌


T = int(input())

for t in range(1, T+1):
    N, W, H = map(int, input().split())

    arr = list(list(map(int, input().split())) for _ in range(H))

    range_list = range(W)
    copy = [0] * N
    max_cnt = 100000000000
    permutation(0)
    print('#%d'%t, max_cnt)