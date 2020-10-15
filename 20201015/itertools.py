from itertools import combinations, permutations
arr = [1, 2, 3, 4, 5]
N = len(arr)
for i in range(N+1):
    comb = list(combinations(arr, i))
    for j in range(len(comb)):
        print(comb[j])
print()
for i in range(N+1):
    permu = list(permutations(arr, i))
    for j in range(len(permu)):
        print(permu[j])
