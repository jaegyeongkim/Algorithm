import sys
sys.stdin = open('가능한 시험 점수.txt')



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    largest = sum(arr)

    portable_list = [0] * (largest+1)
    portable_list[0] = 1

    for i in range(N):
        for j in range(largest, -1, -1):
            if portable_list[j] == 1:
                portable_list[j+arr[i]] = 1

    print('#%d'%t, sum(portable_list))
