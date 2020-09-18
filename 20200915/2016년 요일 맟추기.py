import sys
sys.stdin = open('2016년 요일 맟추기.txt')

T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input().split()))
    # print(arr)
    month = dict()
    date = [0, 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

    for i in range(1, 13):
        month[i] = date[i]
        if i > 1:
            month[i] += month[i-1]
    # print(month)
    print('#%d'%t, ((month[arr[0]] + arr[1])%7+3)%7)
