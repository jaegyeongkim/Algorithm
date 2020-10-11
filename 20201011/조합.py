arr = [1, 2, 3, 4, 5]
N = len(arr)
selected = [0] * N
R = 3

def combintaion(idx):
    if idx == N:
        if sum(selected) == R:
            for i in range(N):
                if selected[i] == 1:
                    print(arr[i], end=' ')
            print()
        return
    selected[idx] = 1
    combintaion(idx+1)
    selected[idx] = 0
    combintaion(idx+1)
combintaion(0)