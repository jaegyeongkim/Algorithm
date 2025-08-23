import sys
sys.stdin = open('2048.txt')
import copy

def permutation(idx):
    if idx == 5:
        new_arr = copy.deepcopy(arr)
        check(copy_, new_arr)
        # print(copy)
        # check([0, 1, 1, 0, 1], new_arr)
        return
    else:
        for i in range(4):
            copy_[idx] = comb[i]
            permutation(idx+1)


def check(copy_, new_arr):
    global max_num

    # print(copy_)
    for d in copy_:
        # print(d)
        if d == 0 or d == 3:
            visited = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if new_arr[i][j] != 0:
                        move(i, j, d, new_arr, visited)
                        # for row in new_arr:
                        #     print(row)
                        # print()

        else:
            visited = [[0] * N for _ in range(N)]
            for i in range(N-1, -1, -1):
                for j in range(N-1, -1, -1):
                    if new_arr[i][j] != 0:
                        move(i, j, d, new_arr, visited)
                        # for row in new_arr:
                        #     print(row)
                        # print()

    num = 0
    for i in range(N):
        for j in range(N):
            if num < new_arr[i][j]:
                num = new_arr[i][j]

    if max_num < num:
        max_num = num
    # print(num)
def move(i, j, d, new_arr, visited):
    while 1:
        ni = i + di[d]
        nj = j + dj[d]

        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            break
        if new_arr[ni][nj] == 0:
            # 0이 아닐떄까지 가고
            # 범위를 안 벗어날때까지 가는 거

            while 1:
                ni += di[d]
                nj += dj[d]

                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    new_arr[ni-di[d]][nj-dj[d]] = new_arr[i][j]
                    new_arr[i][j] = 0
                    break
                else:
                    if new_arr[ni][nj] == new_arr[i][j]:
                        if visited[ni][nj] == 0:
                            new_arr[ni][nj] *= 2
                            visited[ni][nj] = 1
                        else:
                            new_arr[ni-di[d]][nj-dj[d]] = new_arr[i][j]
                        new_arr[i][j] = 0
                        break
                    elif new_arr[ni][nj] == 0:
                        continue
                    elif new_arr[ni][nj] != new_arr[i][j]:
                        new_arr[ni-di[d]][nj-dj[d]] = new_arr[i][j]
                        new_arr[i][j] = 0
                        break


            break
        elif new_arr[ni][nj] == new_arr[i][j]:
            if visited[ni][nj] == 0:
                new_arr[ni][nj] *= 2
                visited[ni][nj] = 1
            else:
                new_arr[ni-di[d]][nj-dj[d]] = new_arr[i][j]
            new_arr[i][j] = 0

            break
        elif new_arr[ni][nj] != new_arr[i][j]:
            new_arr[ni - di[d]][nj - dj[d]] = new_arr[i][j]
            if ni - di[d] == i and nj - dj[d] == j:
                pass
            else:
                new_arr[i][j] = 0
            break
    # print(visited)
N = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
arr = list(list(map(int, input().split())) for _ in range(N))
comb = range(4)
copy_ = [0] * 5
max_num = 0
permutation(0)
print(max_num)