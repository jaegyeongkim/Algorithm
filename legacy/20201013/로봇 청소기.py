import sys
sys.stdin = open('로봇 청소기.txt')

def dfs(robot):

    wash = [[0]* M for _ in range(N)]
    i, j, cd = robot[0], robot[1], robot[2]
    robot = [[i, j, cd]]
    wash[robot[0][0]][robot[0][1]] = 1
    result = 1
    while robot:
        i, j, cd = robot.pop()
        direction_check = [0] * 4
        while 1:

            cd = (cd+3)%4
            ni = i + di[cd]
            nj = j + dj[cd]
            direction_check[cd] = 1

            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and wash[ni][nj] == 0:
                    robot.append([ni, nj, cd])
                    wash[ni][nj] = 1
                    result += 1
                    break

            if sum(direction_check) == 4:
                i -= di[cd]
                j -= dj[cd]

                if arr[i][j] == 1:
                    break
                elif arr[i][j] == 0:
                    robot.append([i, j, cd])
                break


    return result

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for t in range(1, T+1):
    N, M = map(int, input().split())
    robot = list(list(map(int, input().split())))
    arr = list(list(map(int, input().split())) for _ in range(N))

    print(dfs(robot))