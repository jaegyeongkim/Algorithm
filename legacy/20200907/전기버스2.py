import sys
sys.stdin = open('전기버스2.txt')


def charge(idx, cnt, remain):
    global min_cnt
    remain -= 1

    if min_cnt <= cnt:
        return

    if idx == N:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    charge(idx+1, cnt+1, arr[idx])

    if remain > 0:
        charge(idx+1, cnt, remain)


T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))

    N = arr[0]
    min_cnt = 10000
    charge(2, 0, arr[1])
    print('#%d'%t, min_cnt)
