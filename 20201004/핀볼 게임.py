import sys
sys.stdin = open('핀볼 게임.txt')



def dfs(si, sj):
    global max_total
    for d in range(4):
        total = 0
        stack = [[si, sj, d, total]]
        cnt = 0
        while stack:
            i, j, d, total = stack.pop()
            if cnt:
                if i == si and j == sj:
                    break
                elif arr[i][j] == -1:
                    break
            cnt += 1
            ni = i + di[d]
            nj = j + dj[d]
            # print(i, j, d, total)


            # 부딪혔을때
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                d = (d+2) % 4
                if 0 < arr[i][j] <= 5:
                    d = figure_dic[arr[i][j]][d]
                    total += 1
                elif 5 < arr[i][j] <= 10:
                    for ni, nj in figure_dic[arr[i][j]]:
                        if i == ni and j == nj:
                            continue
                        else:
                            i, j = ni, nj
                            break

                stack.append([i, j, d, total+1])

            elif 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == -1:
                    break
                elif ni == si and nj == sj:
                    break

                elif arr[ni][nj] == 0:
                    stack.append([ni, nj, d, total])
                else:
                    if 0 < arr[ni][nj] <= 5:
                        stack.append([ni, nj, figure_dic[arr[ni][nj]][d], total+1])
                    elif 5 < arr[ni][nj] <= 10:
                        for i, j in figure_dic[arr[ni][nj]]:
                            if i == ni and j == nj:
                                continue
                            else:
                                stack.append([i, j, d, total])
                                break


        if max_total < total:
            max_total = total

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌

for t in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    max_total = 0
    figure_dic = {
        1:[2, 3, 1, 0],
        2:[1, 3, 0, 2],
        3:[3, 2, 0, 1],
        4:[2, 0, 3, 1],
        5:[2, 3, 0, 1],
        6:[],
        7:[],
        8:[],
        9:[],
        10:[],
    }

    dfs_list = []
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                figure_dic[arr[i][j]].append([i, j])
            elif arr[i][j] == 0:
                dfs_list.append([i, j])
    # dfs(0, 7)
    # print(dfs_list)
    for i, j in dfs_list:
        dfs(i, j)
        # print()

    print('#%d'%t, max_total)
'''
    1. 방향에 따라 팅기는 거
    2. 웜홈, 블랙홀
    '''