arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
selected = [0] * N
copy = [0] * R


def permutaion(idx):
    if idx == R:
        print(copy)
        return
    else:
        for i in range(N):
            if selected[i] == 0:
                selected[i] = 1
                copy[idx] = arr[i]
                permutaion(idx+1)
                selected[i] = 0
permutaion(0)