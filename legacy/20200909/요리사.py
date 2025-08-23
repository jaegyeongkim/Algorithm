import sys
sys.stdin = open("요리사.txt")

def combination(idx):
    global min_total

    if idx == N:
        if sum(selected) == N/2:
            one_list = []
            zero_list = []

            left_total = 0
            right_total = 0

            for i in range(N):
                if selected[i] == 1:
                    one_list.append(i)
                else:
                    zero_list.append(i)

            for i in one_list:
                for j in one_list:
                    if i != j:
                        left_total += arr[i][j]
            for i in zero_list:
                for j in zero_list:
                    if i != j:
                        right_total += arr[i][j]

            total = abs(right_total-left_total)
            if min_total > total:
                min_total = total


        return

    selected[idx] = 1
    combination(idx+1)
    selected[idx] = 0
    combination(idx+1)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    min_total = 1000000
    selected = [0] * N
    combination(0)
    print('#%d'%t, min_total)