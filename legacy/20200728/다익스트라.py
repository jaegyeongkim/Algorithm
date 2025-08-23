'''
6 11
0 1 3
0 2 7
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
'''
다익스트라는 one to all 로 가는 
출발점에서 모든 점에 대해 가장 짧은 거리를 잡는 거
1. {} 개념으로 잡아주고
2. 거리 무한대로 잡아주고
3. 값이 같은 다른 경로가 나올 수 있음.
4. 
'''
V, E = map(int, input().split())
adj = {i:[] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])
INF = float('inf')
dist = [INF] * V
selected = [0] * V

dist[0] = 0
cnt = 0
while cnt < V-1:
    min = INF
    const_dot = -1
    for i in range(V):
        if selected[i] == 0:
            if min > dist[i]:
                min = dist[i]
                const_dot = i

    selected[const_dot] = 1
    cnt += 1

    for connected_dot, cost in adj[const_dot]:
        if dist[connected_dot] > dist[const_dot] + cost:
            dist[connected_dot] = dist[const_dot] + cost
print(dist)