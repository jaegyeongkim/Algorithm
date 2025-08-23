import sys
sys.stdin = open('벌꿀채취.txt')

def pick(idx, N, selected, total, achieved_honey):
    global max_honey
    if total > C:
        return
    if idx == N:
        honey = 0
        for i in range(N):
            if selected[i] == 1:
                honey += achieved_honey[i] ** 2
        if max_honey < honey:
            max_honey = honey
        return max_honey
    selected[idx] = 1
    total += achieved_honey[idx]
    pick(idx+1, N, selected, total, achieved_honey)
    selected[idx] = 0
    total -= achieved_honey[idx]
    pick(idx + 1, N, selected, total, achieved_honey)

def combination(check):
    global max_honey
    r = check[0]
    c = check[1]
    achieved_honey = [0] * M
    selected = [0] * M
    max_honey = 0
    for m in range(M):
        achieved_honey[m] = arr[r][c+m]


    if sum(achieved_honey) > C:
        pick(0, len(achieved_honey), selected, 0, achieved_honey)
        return max_honey

    total = 0
    for honey in achieved_honey:
        total += honey ** 2
    return total




T = int(input())

for t in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    max_total = 0
    max_honey = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            A_worker = []
            B_worker = []
            for k in range(len(arr)):
                if k+M <= N:
                    if i == j:
                        if k+2*M <= N:
                            A_worker.append([i, k])
                            B_worker.append([j, k+M])
                    else:
                        A_worker.append([i, k])
                        B_worker.append([j, k])
            for m in range(len(A_worker)):
                for n in range(len(B_worker)):
                    if A_worker[m] == B_worker[n]:
                        continue
                    total = combination(A_worker[m]) + combination(B_worker[n])
                    if max_total < total:
                        max_total = total
    print('#%d'%t, max_total)