import sys
sys.stdin = open('Contact.txt')

def bfs(start):
    queue = [[start, 0]]
    max_cnt = 0
    max_num = 0
    visited = [0] * 101
    visited[start] = 1
    while queue:
        current, cnt = queue.pop(0)


        if max_cnt < cnt:
            max_cnt = cnt
            max_num = current
        elif max_cnt == cnt:
            if max_num < current:
                max_num = current

        for j in range(101):
            if adj[current][j] == 1 and visited[j] == 0:
                queue.append([j, cnt+1])
                visited[j] = 1
    return max_num

T = 10
for t in range(1, T+1):
    N, start = map(int, input().split())

    data = list(map(int, input().split()))
    adj = [[0] * 101 for _ in range(101)]

    for i in range(0, N, 2):
        adj[data[i]][data[i+1]] = 1


    print('#%d'%t, bfs(start))