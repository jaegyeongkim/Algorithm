'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

'''
heapq 를 사용하고
O(N^2)의 시간복잡도
크루스칼과 같은 mst 하지만 좀 더 빠름() 그리고 좀 더 어려움
'''
import heapq
V, E = map(int, input().split())
adj = {i:[] for i in range(E)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])
    adj[e].append([s, c])

INF = float('inf')
key = [INF] * V
selected = [0] * V
pq = []
heapq.heappush(pq, (0, 0))

key[0] = 0
result = 0
while pq:
    dist, const_dot = heapq.heappop(pq)
    if selected[const_dot] == 1:
        continue
    result += dist
    selected[const_dot] = 1

    for connected_dot, cost in adj[const_dot]:
        if selected[connected_dot] == 0:
            if key[connected_dot] > cost:
                key[connected_dot] = cost
                heapq.heappush(pq, (key[connected_dot], connected_dot))
print(result)
print(key)