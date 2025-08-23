import sys
sys.stdin = open('길찾기.txt')

def dfs():
    global adj, N, visited
    stack = [0]

    while stack:
        start = stack.pop()
        if start == 99:
            return 1
        s1 = adj[0][start]
        s2 = adj[1][start]
        if s1 != 0:
            stack.append(s1)
        if s2 != 0:
            stack.append(s2)

    return 0
T = 10

for t in range(1, T+1):
    tc, N = map(int, input().split())
    result = 0
    path = list(map(int, input().split()))
    adj = [[0] * 100 for _ in range(2)]
    visited = [0] * 100
    # 유향 그래프로 만들어주기
    for i in range(0, len(path), 2):
        if adj[0][path[i]] == 0:
            adj[0][path[i]] = path[i+1]
        else:
            adj[1][path[i]] = path[i+1]
    result = dfs()
    print('#%d'%t, result)