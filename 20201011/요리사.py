import sys
sys.stdin = open('요리사.txt')

def synergy(combarr):
    total = 0
    for i in combarr:
        for j in combarr:
            if i!=j:
                total += arr[i][j]

    return total

def combination(idx):

    global min_sub
    if min_sub == 0:
        return

    if idx == N:
        if sum(selected) == N//2:
            A_arr = []
            B_arr = []
            for i in range(N):
                if selected[i] == 1:
                    A_arr.append(food_arr[i])
                elif selected[i] == 0:
                    B_arr.append(food_arr[i])

            A_sum = synergy(A_arr)
            B_sum = synergy(B_arr)

            if min_sub > abs(A_sum-B_sum):
                min_sub = abs(A_sum-B_sum)

        return
    selected[idx] = 1
    combination(idx+1)
    selected[idx] = 0
    combination(idx+1)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    food_arr = range(N)
    min_sub = 1000000000000000
    selected = [0] * N
    combination(0)
    print('#%d'%t, min_sub)