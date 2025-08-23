import sys
sys.stdin = open('동철이의 일분배.txt')

def solve(idx, probability):
    global max_probability
    if max_probability >= probability:
        return

    if idx == N:
        if max_probability < probability:
            max_probability = probability
        return

    for i in range(N):
        if selected[i] == 1:
            continue
        selected[i] = 1
        solve(idx+1, probability * arr[idx][i])
        selected[i] = 0

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j]/100
    selected = [0] * N
    max_probability = 0
    solve(0, 1)
    print('#%d %0.6f' %(t, max_probability*100))