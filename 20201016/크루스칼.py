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
MST / 최소신장트리 에서 kruscal 과 prime 이 있는데
가중치가 가장 작게 모든 점들이 연결될 수 있도록 하는 알고리즘을 찾아보자
크루스칼이 좀 더 쉬운 개념의 알고리즘
크루스칼 같은 경우에는
모든 점에 대해 연결했을때 가장 dist 가 짧은 거
필요한 것
dist에 따라 정렬 된
visited 한 배열
O(mlogm) m: 간선의 개수
크루스칼이 쉽긴하지만 시간복잡도가 더 커서 프림이 더 나을 수도...
크루스칼 암기하는 거 너무 어려워요 조금씩 적어봅시다 개념에 대해 생각해보는 걸로
1. 가중치를 오름차순으로 정리한다.
2. 부모 노드를 찾는다. 부모 노드가 안 겹치는 애들의 가중치를 더한다.
'''
def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = p[px]
    else:
        p[px] = p[py]
        if rank[px] == rank[py]:
            rank[py] += 1

V, E = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(E))
arr.sort(key=lambda x:x[2])
p = [0] * V
for i in range(V):
    make_set(i)
rank = [0] * V
mst = []
cnt = 0
result = 0

for i in range(E):
    s, e, c = arr[i][0], arr[i][1], arr[i][2]
    if find_set(s) == find_set(e):
        continue
    cnt += 1
    result += c
    mst.append(arr[i])
    union(s, e)
    if cnt == V-1:
        break
print(mst)
print(result)