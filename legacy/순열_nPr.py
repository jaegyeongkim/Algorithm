arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
copy = [0] * R
selected = [0] * N

def permutation(idx):
    if idx == R:
        print(copy)
        return
    for i in range(N):
        if selected[i] == 0:
            selected[i] = 1
            copy[idx] = arr[i]
            permutation(idx+1)
            selected[i] = 0

permutation(0)