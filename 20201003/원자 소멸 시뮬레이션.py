import sys
sys.stdin = open('원자 소멸 시뮬레이션.txt')

T = int(input())
dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0] # 상 하 좌 우
for t in range(1, T+1):
    N = int(input())
    # x, y, 방향, 에너지
    arr = list(list(map(int, input().split())) for _ in range(N))

    cnt = 0
    total = 0
    K_sum = 0
    for i in range(len(arr)):
        K_sum += arr[i][3]
    before_K_sum = 0

    while K_sum != 0:
        for i in range(len(arr)):
            if arr[i] != 0:
                x = arr[i][0]
                y = arr[i][1]
                d = arr[i][2]
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < -1000 or nx > 1000 or ny < -1000 or ny > 1000:
                    K_sum -= arr[i][3]
                    arr[i] = 0
                    continue

                arr[i][0] = arr[i][0] + dx[arr[i][2]]
                arr[i][1] = arr[i][1] + dy[arr[i][2]]


        arr_dic = {}
        is_add = 0
        # print(arr)

        for i in range(len(arr)):
            if arr[i] != 0:
                if (arr[i][0], arr[i][1]) not in arr_dic:
                    arr_dic[(arr[i][0], arr[i][1])] = [arr[i][3], i]
                else:
                    if is_add == 0:
                        total += arr_dic[(arr[i][0], arr[i][1])][0]
                        K_sum -= arr_dic[(arr[i][0], arr[i][1])][0]
                        arr[arr_dic[(arr[i][0], arr[i][1])][1]] = 0
                        is_add = 1

                    total += arr[i][3]
                    K_sum -= arr[i][3]
                    arr[i] = 0



    print('#%d'%t, total)