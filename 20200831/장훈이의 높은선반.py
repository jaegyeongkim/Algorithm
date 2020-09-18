import sys
sys.stdin = open('장훈이.txt')



def powerset(idx, total):
    global result

    if idx == N:
        if total >= B:
            if result > total:
                result = total
        return

    if result < total:
        return

    selected[idx] = 1
    total += arr[idx]
    powerset(idx+1, total)

    selected[idx] = 0
    total -= arr[idx]
    powerset(idx+1, total)

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    selected = [0] * N
    result = float('inf')
    powerset(0, 0)
    print('#%d'%t, result-B)