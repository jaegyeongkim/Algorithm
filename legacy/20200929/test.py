import sys
sys.stdin = open('퍼펙트 셔플.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    # print(arr)
    if N%2:
        divide = N//2+1
    else:
        divide = N//2
    front = arr[:divide]
    back = arr[divide:]
    new_arr = []
    while 1:        
        new_arr.append(front.pop(0))
        if len(back) == 0:
            break
        
        new_arr.append(back.pop(0))
        if len(front) == 0:
            break
        
    print('#%d'%t, end=' ')
    for n in range(len(new_arr)):
        if n == N-1:
            print(new_arr[n])
        else:
            print(new_arr[n], end=' ')