import sys
sys.stdin = open('스타트와 링크.txt')

def combination(idx):
    global min_total
    if min_total == 0:
        return
    if idx == N:
        if sum(selected) == N/2:
            team1 = []
            team2 = []
            for i in range(N):
                if selected[i]:
                    team1.append(max_list[i])
                else:
                    team2.append(max_list[i])
            total1 = 0
            total2 = 0
            for i in range(len(team1)):
                for j in range(len(team1)):
                    total1 += arr[team1[i]][team1[j]]

            for i in range(len(team2)):
                for j in range(len(team2)):
                    total2 += arr[team2[i]][team2[j]]
            total = abs(total1-total2)
            if min_total > total:
                min_total = total
        return

    selected[idx] = 1
    combination(idx+1)
    selected[idx] = 0
    combination(idx + 1)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    max_list = range(N)
    selected = [0] * N

    min_total = 10000000000000000
    combination(0)
    print(min_total)
