arr = [1, 2, 3, 4, 5]
N = len(arr)
selected = [0] * N
R = 3

def combination(idx):
    if idx == N:
        if sum(selected) == R:
            for i in range(N):
                if selected[i] == 1:
                    print(arr[i], end=' ')
            print()
        return
    selected[idx] = 1
    combination(idx+1)
    selected[idx] = 0
    combination(idx+1)
combination(0)