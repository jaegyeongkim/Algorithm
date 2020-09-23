import sys
sys.stdin = open('보호 필름.txt')


def check(arr):
    is_K = [0] * W
    for j in range(W):
        continuous = arr[0][j]
        continuous_cnt = 1
        for i in range(1, D):
            if continuous == arr[i][j]:
                continuous_cnt += 1
                if continuous_cnt == K:
                    is_K[j] = 1
                    break
            else:
                continuous = arr[i][j]
                continuous_cnt = 1

        if continuous_cnt < K:
            return
    return 1


def powerset(idx):
    if idx == D:
        power_list = []
        for i in range(D):
            if selected[i] == 1:
                power_list.append(i)
        if len(power_list) > 0:
            powerset_list.append(power_list)
        return

    selected[idx] = 0
    powerset(idx + 1)
    selected[idx] = 1
    powerset(idx + 1)

def power_list_powerset(idx, N, selected, arr, arr_list):
    if idx == N:
        small_list = []
        for i in range(N):
            if selected[i] == 1:
                small_list.append(arr[i])
        arr_list.append(small_list)
        return arr_list
    selected[idx] = 0
    power_list_powerset(idx+1, N, selected, arr, arr_list)
    selected[idx] = 1
    power_list_powerset(idx + 1, N, selected, arr, arr_list)
    return arr_list

def change(power_list):
    N = len(power_list)
    selected = [0] * N
    arr_list = []
    arr_list = power_list_powerset(0, N, selected, power_list, arr_list)
    arr_list.sort(key=len)

    origin_coloumn = [0] * D
    for i in power_list:
        origin_coloumn[i] = origin_arr[i]

    for row in arr_list:
        for j in range(len(power_list)):
            if power_list[j] in row:
                origin_arr[power_list[j]] = [0] * W
            else:
                origin_arr[power_list[j]] = [1] * W


        result0 = check(origin_arr)
        for k in power_list:
            origin_arr[k] = origin_coloumn[k]

        if result0:
            return N
        for j in range(len(power_list)):
            if power_list[j] in row:
                origin_arr[power_list[j]] = [1] * W
            else:
                origin_arr[power_list[j]] = [0] * W
        result1 = check(origin_arr)
        for k in power_list:
            origin_arr[k] = origin_coloumn[k]
        if result1:
            return N


    return float('inf')

T = int(input())

for t in range(1, T + 1):
    D, W, K = map(int, input().split())
    origin_arr = list(list(map(int, input().split())) for _ in range(D))

    if K == 1:
        print('#%d' %t, 0)
        continue


    result = check(origin_arr)
    if result == 1:
        print('#%d' %t, 0)
        continue

    selected = [0] * D
    powerset_list = []
    powerset(0)
    powerset_list.sort(key=len)

    min_cnt = 100000000000000
    for i in range(len(powerset_list)):
        cnt = change(powerset_list[i])
        if min_cnt > cnt:
            print('#%d'%t, cnt)
            break
