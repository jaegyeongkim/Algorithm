import sys
sys.stdin = open('새샘이의 7-3-5게임.txt')

def combination(idx, total):
    if idx == N:
        if sum(selected) == 3:
            big_number.append(total)
            # for i in range(N):
            #     if selected[i] == 1:
            #         print(arr[i], end=' ')
            # print()
        return

    if len(big_number) > 100:
        return
    selected[idx] = 1
    total += arr[idx]
    combination(idx + 1, total)

    selected[idx] = 0
    total -= arr[idx]
    combination(idx + 1, total)


T = int(input())

for t in range(1, T + 1):
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    N = len(arr)
    selected = [0] * N
    # print(arr)
    big_number = []
    combination(0, 0)
    big_number.sort(reverse=True)

    # print(big_number)

    check = []
    cnt = 0
    result = 0
    for i in big_number:
        if i not in check:
            check.append(i)
            cnt += 1
            if cnt == 5:
                result = i
                break
    print('#%d'%t, result)
