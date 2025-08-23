import sys
sys.stdin = open('길찾기.txt')

def dfs(v):
    global adj, N, visited
    if v == 99:
        return 1
    if visited[v] == 1:
        return 0

    visited[v] = 1 # 해당 지점을 방문했음을 표시
    result1 = 0
    result2 = 0
    if adj[0][v] != 0:
        result1 = dfs(adj[0][v])
    if adj[1][v] != 0:
        result2 = dfs(adj[1][v])

    return result1 or result2
T = 10

for t in range(1, T+1):
    tc, N = map(int, input().split())
    result = 0
    path = list(map(int, input().split()))
    max_idx = max(path)
    adj = [[0] * 100 for _ in range(2)]
    visited = [0] * 100
    for i in range(0, len(path), 2):
        if adj[0][path[i]] == 0:
            adj[0][path[i]] = path[i+1]
        else:
            adj[1][path[i]] = path[i+1]
    result = dfs(0)
    print('#%d'%t,result)