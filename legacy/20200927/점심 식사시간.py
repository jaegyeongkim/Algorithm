import sys
sys.stdin = open('점심 식사시간.txt')

def powerset(idx):
    if idx == P:
        case = []
        for i in range(P):
            if selected[i] == 1:
                case.append(stair_position[0])
            else:
                case.append(stair_position[1])
        total_case.append(case)
        return
    selected[idx] = 1
    powerset(idx+1)
    selected[idx] = 0
    powerset(idx+1)

def move(case):
    time = []
    for i in range(len(case)):
        distance = abs(people_position[i][0] - case[i][0]) + abs(people_position[i][1] - case[i][1])
        time.append([distance, people_position[i][0], people_position[i][1], case[i][2]])

    time.sort(key=lambda x:x[0])
    exit_list1 = [0] * (time[-1][0]+max_stair+1000)
    exit_list2 = [0] * (time[-1][0]+max_stair+1000)
    for i in range(len(time)):
        if time[i][3] == stair_position[0][2]:
            if exit_list1[time[i][0]+1] == 3:
                j = 0
                while 1:
                    j += 1
                    if exit_list1[time[i][0]+1+j] < 3:
                        break
                for k in range(1, arr[stair_position[0][0]][stair_position[0][1]]+1):
                    exit_list1[time[i][0]+k+j] += 1

            else:
                for k in range(1, arr[stair_position[0][0]][stair_position[0][1]] + 1):
                    exit_list1[time[i][0]+k] += 1
        else:
            if exit_list2[time[i][0]+1] == 3:
                j = 0
                while 1:
                    j += 1
                    if exit_list2[time[i][0]+1+j] < 3:
                        break
                for k in range(1, arr[stair_position[1][0]][stair_position[1][1]] + 1):
                    exit_list2[time[i][0]+k+j] += 1

            else:
                for k in range(1, arr[stair_position[1][0]][stair_position[1][1]] + 1):
                    exit_list2[time[i][0] + k] += 1
    for i in range(len(exit_list1)-1, -1, -1):
        if exit_list1[i] > 0:
            return i+1
        if exit_list2[i] > 0:
            return i+1


T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌

for t in range(1, T+1):
    N = int(input())

    arr = list(list(map(int, input().split())) for _ in range(N))
    people_position = []
    stair_position = []
    max_stair = 0
    P = 0
    stair_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people_position.append([i, j])
                P += 1
            if arr[i][j] > 1:
                stair_position.append([i, j, stair_cnt])
                stair_cnt += 1
                if max_stair < arr[i][j]:
                    max_stair = arr[i][j]
    cnt = 0
    selected = [0] * P
    total_case = []
    powerset(0)
    min_cnt = 10000000000
    for case in total_case:
        current = move(case)
        if min_cnt > current:
            min_cnt = current
    print('#%d'%t, min_cnt)