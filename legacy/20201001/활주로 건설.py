import sys
sys.stdin = open('활주로  건설.txt')

def check(pick):
    # print(pick)
    selected = [0] * N
    for i in range(len(pick)-1):
        if pick[i] == pick[i+1]:
            continue
        # print(i)
        # 왼쪽이 더 높을때
        if pick[i] == pick[i+1]+1:
            if i+X < N:
                for x in range(1, X+1):
                    if selected[i+x] == 1:
                        return 0

                    if pick[i+1] != pick[i+x]:
                        return 0
                    else:
                        selected[i+x] = 1
            else:
                return 0
        # 오른쪽이 더 높을때
        elif pick[i]+1 == pick[i+1]:
            if 0 <= i+1-X:
                for x in range(X):
                    if selected[i-x] == 1:
                        return 0

                    if pick[i] != pick[i-x]:
                        return 0
                    else:
                        selected[i-x] = 1
            else:
                return 0
        else:
            return 0
    # print(1, pick)
    return 1




T = int(input())

for t in range(1, T+1):
    N, X = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    new_arr = list(map(list, zip(*arr)))
    # for row in arr:
    #     print(row)
    # print()
    total = 0
    for i in range(N):
        same_1 = 0
        same_2 = 0
        for j in range(1, N):
            if arr[i][j] == arr[i][0]:
                same_1 += 1
            else:
                total += check(arr[i])
                break

        for j in range(1, N):
            if new_arr[i][j] == new_arr[i][0]:
                same_2 += 1
            else:
                total += check(new_arr[i])
                break

        if same_1 == N-1:
            total += 1

        if same_2 == N-1:
            total += 1

    print('#%d'%t, total)
