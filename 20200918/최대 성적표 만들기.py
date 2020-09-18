import sys
sys.stdin = open('최대 성적표 만들기.txt')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    # print(arr)
    result = 0
    for i in range(K):
        result += arr[i]
    print('#%d'%t,result)