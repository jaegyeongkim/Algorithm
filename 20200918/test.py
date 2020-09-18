import sys
sys.stdin = open('영준이와 신비한 뿔의 숲.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 뿔 / M마리의 짐승
    for i in range(M+1):
        tri = i
        uni = M-i
        if tri*2 + uni == N:
            break
    print('#%d'%t, uni, tri)