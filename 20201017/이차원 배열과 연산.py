import sys
sys.stdin = open('이차원 배열과 연산.txt')
def calculation_R(arr):
    new_arr = [[] for _ in range(len(arr))]
    max_length = 0
    for i in range(len(arr)):
        new_row = [[0]*2 for _ in range(max(arr[i])+1)]

        for k in range(1, len(new_row)):
            new_row[k][0] = k
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                continue
            new_row[arr[i][j]][1] += 1
        new_row.sort(key=lambda x:x[1])

        for r in range(len(new_row)):
            if new_row[r][1] == 0:
                continue
            new_arr[i].append(new_row[r][0])
            new_arr[i].append(new_row[r][1])
        length = len(new_arr[i])
        if max_length < length:
            max_length = length
    for i in range(len(new_arr)):
        while len(new_arr[i]) < max_length:
            new_arr[i].append(0)


    return new_arr

def calculation_C(arr):
    new_arr = [[] for _ in range(len(arr[0]))]
    copy_arr = [[0] * len(arr) for _ in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            copy_arr[j][i] = arr[i][j]
    max_length = 0
    for i in range(len(copy_arr)):
        new_row = [[0]*2 for _ in range(max(copy_arr[i])+1)]
        for k in range(1, len(new_row)):
            new_row[k][0] = k

        for j in range(len(copy_arr[i])):
            if copy_arr[i][j] == 0:
                continue
            new_row[copy_arr[i][j]][1] += 1
        new_row.sort(key=lambda x:x[1])
        for r in range(len(new_row)):
            if new_row[r][1] == 0:
                continue
            new_arr[i].append(new_row[r][0])
            new_arr[i].append(new_row[r][1])
        length = len(new_arr[i])
        if max_length < length:
            max_length = length

    for i in range(len(new_arr)):
        while len(new_arr[i]) < max_length:
            new_arr[i].append(0)
    arr = [[0]*len(new_arr) for _ in range(len(new_arr[0]))]
    for i in range(len(new_arr[0])):
        for j in range(len(new_arr)):
            arr[i][j] = new_arr[j][i]
    return arr

r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = list(list(map(int, input().split())) for _ in range(3))
cnt = 0

if arr[r][c] == k:
    print(cnt)
else:
    while cnt < 100:
        if len(arr) > 100:
            arr = arr[:100]
        if len(arr[0]) > 100:
            for i in range(len(arr)):
                arr[i] = arr[i][:100]

        cnt += 1
        if len(arr) >= len(arr[0]):
            arr = calculation_R(arr)
        else:
            arr = calculation_C(arr)
        if len(arr) <= r:
            continue
        if len(arr[0]) <= c:
            continue
        if arr[r][c] == k:
            print(cnt)
            break
    else:
        print(-1)
