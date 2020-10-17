from collections import deque
from itertools import combinations, permutations
import copy

arr = [1, 2, 3, 4, 5]
N = len(arr)
for i in range(N+1):
    combi = list(combinations(arr, i))
    for j in range(len(combi)):
        print(combi[j])

for i in range(N+1):
    permu = list(permutations(arr, i))
    for j in range(len(permu)):
        print(permu[j])
